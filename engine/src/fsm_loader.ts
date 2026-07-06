import * as fs from 'fs';
import * as path from 'path';
import * as yaml from 'js-yaml';

export interface StateMachineConfig {
    initial_state: string;
    states: string[];
    terminal_states: string[];
    transitions: Array<{
        from: string;
        event: string;
        to: string;
        actor: string;
        guards?: string[];
        required_artifacts?: string[];
    }>;
    execution_modes: Record<string, any>;
}

export class FSMLoader {
    public config: StateMachineConfig;

    constructor(yamlPath: string) {
        if (!fs.existsSync(yamlPath)) {
            throw new Error(`State machine file not found at ${yamlPath}`);
        }
        const fileContents = fs.readFileSync(yamlPath, 'utf8');
        this.config = yaml.load(fileContents) as StateMachineConfig;
    }

    getInitialState(): string {
        return this.config.initial_state;
    }

    getTransitionsFrom(state: string) {
        return this.config.transitions.filter(t => t.from === state);
    }

    isValidState(state: string): boolean {
        return this.config.states.includes(state);
    }
}
