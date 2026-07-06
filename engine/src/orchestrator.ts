import { FSMLoader } from './fsm_loader';
import { AuditorLogger } from './logger';

export class Orchestrator {
    private fsm: FSMLoader;
    private logger: AuditorLogger;
    private currentState: string;
    private taskInput: string;
    private riskTier: 'low' | 'medium' | 'high' | 'critical' = 'low';

    constructor(fsmPath: string, taskInput: string, riskTier: 'low' | 'medium' | 'high' | 'critical' = 'low') {
        this.fsm = new FSMLoader(fsmPath);
        this.logger = new AuditorLogger();
        this.currentState = this.fsm.getInitialState();
        this.taskInput = taskInput;
        this.riskTier = riskTier;
    }

    public async runSimulation() {
        this.logger.info(`Starting Orchestrator Simulation`, { task: this.taskInput, riskTier: this.riskTier });
        
        let steps = 0;
        const maxSteps = 50; // Prevent infinite loops
        
        while (!this.fsm.config.terminal_states.includes(this.currentState) && steps < maxSteps) {
            steps++;
            this.logger.info(`[STATE] Entered: ${this.currentState}`);
            
            // Artificial delay to simulate LLM processing and avoid rate limits
            await this.sleep(1000);

            const possibleTransitions = this.fsm.getTransitionsFrom(this.currentState);
            if (possibleTransitions.length === 0) {
                this.logger.error(`Deadlock: No transitions from ${this.currentState}`);
                break;
            }

            // Simple Simulation Logic: Pick the first successful/forward transition
            // In a real run, this would be decided by LLM outputs and schema validation
            let nextTransition = possibleTransitions[0];

            // Special handling for risk_tier routing in simulation
            if (this.currentState === 'CONTEXT_RESOLVED') {
                if (this.riskTier === 'low') {
                    nextTransition = possibleTransitions.find(t => t.event === 'route_fast_track') || nextTransition;
                } else {
                    nextTransition = possibleTransitions.find(t => t.event === 'submit_plan') || nextTransition;
                }
            } else if (this.currentState === 'PLAN_READY') {
                if (this.riskTier === 'medium') {
                    nextTransition = possibleTransitions.find(t => t.event === 'route_for_normal_approval') || nextTransition;
                } else {
                    nextTransition = possibleTransitions.find(t => t.event === 'route_for_enterprise_approval') || nextTransition;
                }
            } else if (possibleTransitions.length > 1) {
                // If multiple paths (e.g., pass vs fail), pick the "pass" or "success" path for simulation
                nextTransition = possibleTransitions.find(t => 
                    !t.event.includes('fail') && 
                    !t.event.includes('reject') && 
                    !t.event.includes('defer') && 
                    !t.event.includes('abort') && 
                    !t.event.includes('agent_failure') && 
                    !t.event.includes('conflict') &&
                    !t.event.includes('blocked')
                ) || possibleTransitions[0];
            }

            this.logger.info(`[TRANSITION] Firing event: ${nextTransition.event} (Actor: ${nextTransition.actor})`);
            
            if (nextTransition.required_artifacts && nextTransition.required_artifacts.length > 0) {
                this.logger.info(`[ARTIFACTS] Mocking generation of: ${nextTransition.required_artifacts.join(', ')}`);
            }

            this.currentState = nextTransition.to;
        }

        if (this.fsm.config.terminal_states.includes(this.currentState)) {
            this.logger.info(`[TERMINAL] Reached terminal state: ${this.currentState}. Simulation Complete.`);
        } else if (steps >= maxSteps) {
            this.logger.error(`[TIMEOUT] Reached max steps limit. Possible infinite loop.`);
        }
    }

    private sleep(ms: number) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}
