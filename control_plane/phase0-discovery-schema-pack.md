# Phase 0 Discovery Schema Pack

This companion pack formalizes the intermediate discovery artifacts that precede the canonical `business_feasibility_report`. These artifacts are intended for use by the **Business Strategist / Market Analyst** during Phase 0 and provide structured inputs to the final feasibility decision.

## Included schemas

- `market_scan.schema.json` — captures market demand signals, segment attractiveness, trend direction, and high-level opportunity framing
- `competitor_map.schema.json` — captures direct, indirect, substitute, and internal alternatives along with strategic positioning gaps
- `uvp_canvas.schema.json` — captures the target customer, problem framing, differentiated value drivers, and draft UVP statement
- `business_feasibility_report.schema.json` — synthesizes all discovery findings into the canonical go / conditional_go / defer / no_go decision artifact

## Suggested Phase 0 flow

1. Produce `market_scan`
2. Produce `competitor_map`
3. Produce `uvp_canvas`
4. Synthesize into `business_feasibility_report`
5. Submit feasibility decision to the orchestrator

## Control-plane interpretation

These discovery artifacts are informative and preparatory. The **orchestrator admission gate** should key off `business_feasibility_report`, not the intermediate artifacts directly. However, governance policy may require that a feasibility report reference or embed evidence derived from the intermediate discovery artifacts.

## Recommended next step

The next high-value improvement would be to add example fixtures for `market_scan`, `competitor_map`, and `uvp_canvas`, plus negative fixtures for each, so Phase 0 can be validated with the same rigor as the downstream control-plane artifacts.
