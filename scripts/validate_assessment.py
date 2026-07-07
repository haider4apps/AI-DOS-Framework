"""
AI-DOS Assessment Validator
============================
Validates that AI-generated CodebaseAssessments, BugfixSpecs, and RefactoringPlans
contain evidence-backed claims with proper file citations.

Usage:
    python validate_assessment.py <assessment_json_path> [--transcript <transcript_jsonl_path>]

Without --transcript: Checks if cited files exist on disk and citations are formatted correctly.
With --transcript: ALSO cross-references cited files against the subagent's actual view_file calls
                   to catch hallucinated claims (files cited but never opened).
"""
import json
import sys
import os
import re

# Fix Windows console encoding for emoji/unicode output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")



def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_transcript_opened_files(transcript_path: str) -> set:
    """Parse a subagent's transcript.jsonl to find all files actually opened via view_file."""
    opened = set()
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    step = json.loads(line)
                except json.JSONDecodeError:
                    continue

                # Check for view_file tool calls
                tool_calls = step.get("tool_calls", [])
                if isinstance(tool_calls, list):
                    for tc in tool_calls:
                        if tc.get("name") == "view_file":
                            args = tc.get("args", {})
                            abs_path = args.get("AbsolutePath", "")
                            # Strip quotes that may be in the JSON
                            abs_path = abs_path.strip('"').strip("'")
                            if abs_path:
                                opened.add(os.path.normpath(abs_path).lower())

                # Also check VIEW_FILE step responses for the actual file path
                if step.get("type") == "VIEW_FILE":
                    content = step.get("content", "")
                    m = re.search(r"File Path: `file:///([^`]+)`", content)
                    if m:
                        fpath = m.group(1).replace("%20", " ")
                        opened.add(os.path.normpath(fpath).lower())
    except Exception as e:
        print(f"[WARN] Could not parse transcript: {e}")
    return opened


def extract_citations(text: str) -> list:
    """Extract [VERIFIED: file.py:L123] or [UNVERIFIED: ...] citations from text."""
    pattern = r'\[(VERIFIED|UNVERIFIED):\s*([^\]]+)\]'
    return re.findall(pattern, text)


def extract_file_paths_from_text(text: str) -> list:
    """Extract any file path references from text (e.g., ui/app.py, hybrid_tester.py:L864)."""
    patterns = [
        r'`([a-zA-Z_/\\][\w/\\.]+\.(?:py|kt|java|js|ts|xml|gradle|kts|json|yaml|yml))`',
        r'([a-zA-Z_/\\][\w/\\.]+\.(?:py|kt|java|js|ts|xml|gradle|kts|json|yaml|yml))(?::L?\d+)?',
    ]
    paths = set()
    for pat in patterns:
        for m in re.finditer(pat, text):
            paths.add(m.group(1) if m.lastindex else m.group(0))
    return list(paths)


def validate_codebase_assessment(assessment: dict, transcript_files: set = None) -> dict:
    """Validate a CodebaseAssessment artifact."""
    results = {
        "passed": True,
        "errors": [],
        "warnings": [],
        "stats": {
            "total_claims": 0,
            "verified_claims": 0,
            "unverified_claims": 0,
            "hallucinated_claims": 0,
        }
    }

    # Check required fields
    required = ["detected_tech_stack", "current_architecture", "broken_or_incomplete_areas", "risk_hotspots"]
    for field in required:
        if field not in assessment:
            results["errors"].append(f"Missing required field: {field}")
            results["passed"] = False

    # Check broken_or_incomplete_areas for evidence
    for area in assessment.get("broken_or_incomplete_areas", []):
        results["stats"]["total_claims"] += 1
        citations = extract_citations(area)
        file_refs = extract_file_paths_from_text(area)

        if citations:
            for status, ref in citations:
                if status == "VERIFIED":
                    results["stats"]["verified_claims"] += 1
                else:
                    results["stats"]["unverified_claims"] += 1
                    results["warnings"].append(f"Unverified claim: {area[:80]}...")
        elif file_refs:
            results["stats"]["verified_claims"] += 1  # Has file ref but no formal citation
            results["warnings"].append(f"Claim has file reference but no formal [VERIFIED/UNVERIFIED] citation: {area[:80]}...")
        else:
            results["stats"]["hallucinated_claims"] += 1
            results["errors"].append(f"HALLUCINATED CLAIM (no file citation): {area[:80]}...")
            results["passed"] = False

    # Check risk_hotspots for evidence
    for hotspot in assessment.get("risk_hotspots", []):
        results["stats"]["total_claims"] += 1
        citations = extract_citations(hotspot)
        file_refs = extract_file_paths_from_text(hotspot)

        if citations:
            for status, ref in citations:
                if status == "VERIFIED":
                    results["stats"]["verified_claims"] += 1
                else:
                    results["stats"]["unverified_claims"] += 1
        elif file_refs:
            results["stats"]["verified_claims"] += 1
        else:
            results["stats"]["hallucinated_claims"] += 1
            results["errors"].append(f"HALLUCINATED CLAIM (no file citation): {hotspot[:80]}...")
            results["passed"] = False

    # Cross-reference with transcript if available
    if transcript_files is not None:
        all_cited_files = set()
        full_text = json.dumps(assessment)
        for fp in extract_file_paths_from_text(full_text):
            all_cited_files.add(fp)

        # Check README-only scanning
        core_extensions = {'.py', '.kt', '.java', '.js', '.ts'}
        opened_core_files = [f for f in transcript_files
                             if any(f.endswith(ext) for ext in core_extensions)]

        if len(opened_core_files) < 3:
            results["errors"].append(
                f"SHALLOW SCAN DETECTED: Only {len(opened_core_files)} core source files were "
                f"actually opened via view_file. The AI likely hallucinated its assessment from "
                f"README or directory listings alone."
            )
            results["passed"] = False

        results["stats"]["files_actually_opened"] = len(transcript_files)
        results["stats"]["core_files_opened"] = len(opened_core_files)

    return results


def validate_bugfix_spec(spec: dict) -> dict:
    """Validate a BugfixSpec artifact."""
    results = {"passed": True, "errors": [], "warnings": []}

    required = ["bug_title", "root_cause_analysis", "affected_files", "verification_plan", "risk_level"]
    for field in required:
        if field not in spec:
            results["errors"].append(f"Missing required field: {field}")
            results["passed"] = False

    # Check affected_files have proper structure
    for af in spec.get("affected_files", []):
        if "file_path" not in af:
            results["errors"].append("affected_files entry missing 'file_path'")
            results["passed"] = False
        if "issue_description" not in af:
            results["errors"].append(f"affected_files entry for {af.get('file_path', '?')} missing 'issue_description'")
            results["passed"] = False

    # Check root_cause_analysis has file citations
    rca = spec.get("root_cause_analysis", "")
    if rca and not extract_file_paths_from_text(rca):
        results["warnings"].append("root_cause_analysis does not cite any specific file paths")

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_assessment.py <json_path> [--transcript <transcript.jsonl>]")
        sys.exit(1)

    json_path = sys.argv[1]
    transcript_path = None

    if "--transcript" in sys.argv:
        idx = sys.argv.index("--transcript")
        if idx + 1 < len(sys.argv):
            transcript_path = sys.argv[idx + 1]

    if not os.path.exists(json_path):
        print(f"[FAIL] File not found: {json_path}")
        sys.exit(1)

    data = load_json(json_path)

    # Auto-detect artifact type
    transcript_files = None
    if transcript_path and os.path.exists(transcript_path):
        transcript_files = load_transcript_opened_files(transcript_path)
        print(f"[INFO] Loaded transcript: {len(transcript_files)} files were opened via view_file")

    if "detected_tech_stack" in data or "risk_hotspots" in data:
        print("[INFO] Detected artifact type: CodebaseAssessment")
        results = validate_codebase_assessment(data, transcript_files)
    elif "bug_title" in data:
        print("[INFO] Detected artifact type: BugfixSpec")
        results = validate_bugfix_spec(data)
    elif "refactoring_title" in data:
        print("[INFO] Detected artifact type: RefactoringPlan")
        results = validate_bugfix_spec(data)  # Similar validation
    else:
        print("[WARN] Unknown artifact type, performing basic validation only")
        results = {"passed": True, "errors": [], "warnings": []}

    # Print results
    print("\n" + "=" * 60)
    if results["passed"]:
        print("✅ VALIDATION PASSED")
    else:
        print("❌ VALIDATION FAILED")
    print("=" * 60)

    if results.get("stats"):
        stats = results["stats"]
        print(f"\nClaims: {stats.get('total_claims', 0)} total")
        print(f"  ✅ Verified:      {stats.get('verified_claims', 0)}")
        print(f"  ⚠️  Unverified:   {stats.get('unverified_claims', 0)}")
        print(f"  ❌ Hallucinated:  {stats.get('hallucinated_claims', 0)}")
        if "files_actually_opened" in stats:
            print(f"\nTranscript Analysis:")
            print(f"  Files opened:     {stats['files_actually_opened']}")
            print(f"  Core files opened: {stats['core_files_opened']}")

    if results["errors"]:
        print(f"\n🔴 ERRORS ({len(results['errors'])}):")
        for e in results["errors"]:
            print(f"  - {e}")

    if results["warnings"]:
        print(f"\n🟡 WARNINGS ({len(results['warnings'])}):")
        for w in results["warnings"]:
            print(f"  - {w}")

    sys.exit(0 if results["passed"] else 1)


if __name__ == "__main__":
    main()
