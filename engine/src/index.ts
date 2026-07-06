import * as path from 'path';
import { Orchestrator } from './orchestrator';

async function main() {
    const fsmPath = path.resolve(__dirname, '../../control_plane/state_machine.yaml');
    
    // Test 1: Fast Mode (Low Risk)
    console.log("=== RUNNING FAST MODE SIMULATION ===");
    const engineFast = new Orchestrator(fsmPath, "Change the login button to red", "low");
    await engineFast.runSimulation();

    console.log("\n=== RUNNING ENTERPRISE MODE SIMULATION ===");
    // Test 2: Enterprise Mode (High Risk)
    const engineEnterprise = new Orchestrator(fsmPath, "Implement OAuth2 and database migration", "high");
    await engineEnterprise.runSimulation();
}

main().catch(err => {
    console.error("Fatal Error:", err);
});
