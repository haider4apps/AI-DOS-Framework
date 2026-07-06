import * as fs from 'fs';
import * as path from 'path';
import Ajv2020 from 'ajv/dist/2020';

const ajv = new Ajv2020({ strict: false });

const basePath = path.join(__dirname, '../../');
const manifestPath = path.join(basePath, 'fixtures/fixture_manifest.json');
const schemasPath = path.join(basePath, 'schemas');
const fixturesPath = path.join(basePath, 'fixtures');

const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

console.log("=== AI-DOS FIXTURE VALIDATION REPORT ===");

let passed = 0;
let failed = 0;

for (const entry of manifest.entries) {
    if (!entry.schema_file) continue; // Skip entries without a local schema file

    console.log(`\nValidating Artifact: ${entry.artifact_name}`);
    const schemaFile = path.join(schemasPath, entry.schema_file);
    
    if (!fs.existsSync(schemaFile)) {
        console.log(`[ERROR] Schema file missing: ${schemaFile}`);
        failed++;
        continue;
    }

    const schema = JSON.parse(fs.readFileSync(schemaFile, 'utf8'));
    const validate = ajv.compile(schema);

    // 1. Positive Fixture Test
    if (entry.positive_fixture) {
        const posFile = path.join(fixturesPath, entry.positive_fixture);
        if (fs.existsSync(posFile)) {
            const posData = JSON.parse(fs.readFileSync(posFile, 'utf8'));
            const valid = validate(posData);
            if (valid) {
                console.log(`  [PASS] Positive Fixture: ${entry.positive_fixture} validated successfully.`);
                passed++;
            } else {
                console.log(`  [FAIL] Positive Fixture: ${entry.positive_fixture} failed validation.`);
                console.log(`         Errors:`, validate.errors);
                failed++;
            }
        } else {
            console.log(`  [WARNING] Positive fixture file missing: ${posFile}`);
        }
    }

    // 2. Negative Fixture Test
    if (entry.negative_fixture) {
        const negFile = path.join(fixturesPath, entry.negative_fixture);
        if (fs.existsSync(negFile)) {
            const negData = JSON.parse(fs.readFileSync(negFile, 'utf8'));
            const valid = validate(negData);
            if (!valid) {
                console.log(`  [PASS] Negative Fixture: ${entry.negative_fixture} successfully rejected as expected.`);
                passed++;
            } else {
                console.log(`  [FAIL] Negative Fixture: ${entry.negative_fixture} incorrectly passed validation!`);
                failed++;
            }
        } else {
            console.log(`  [WARNING] Negative fixture file missing: ${negFile}`);
        }
    }
}

console.log(`\n=== SUMMARY ===`);
console.log(`Total Checks Passed: ${passed}`);
console.log(`Total Checks Failed: ${failed}`);

if (failed > 0) {
    process.exit(1);
}
