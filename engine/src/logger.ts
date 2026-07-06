import * as fs from 'fs';
import * as path from 'path';

export class AuditorLogger {
    private logFile: string;

    constructor(logFilename: string = 'execution_audit.log') {
        const logDir = path.join(__dirname, '../../logs');
        if (!fs.existsSync(logDir)) {
            fs.mkdirSync(logDir, { recursive: true });
        }
        this.logFile = path.join(logDir, logFilename);
        
        // Initialize the log file for this run
        fs.writeFileSync(this.logFile, `=== AI-DOS Execution Audit Log ===\nStarted at: ${new Date().toISOString()}\n\n`);
    }

    info(message: string, data?: any) {
        this.write('INFO', message, data);
    }

    warn(message: string, data?: any) {
        this.write('WARN', message, data);
    }

    error(message: string, data?: any) {
        this.write('ERROR', message, data);
    }

    private write(level: string, message: string, data?: any) {
        const timestamp = new Date().toISOString();
        let logLine = `[${timestamp}] [${level}] ${message}\n`;
        if (data) {
            logLine += `${JSON.stringify(data, null, 2)}\n`;
        }
        
        // Write to file
        fs.appendFileSync(this.logFile, logLine);
        
        // Also print to console so Antigravity can watch it
        console.log(`[${level}] ${message}`);
    }
}
