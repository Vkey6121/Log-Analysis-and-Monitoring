import time
import random
import sys

class GenerateLogs:
    """
    A class for generating logs.
    This class provides generate logs to test the log analysis and monitoring script.

    Attributes:
        levels: A list of log levels.
        messages: A list of log messages.
        log_file: A string representing the log file path.
        num_logs: An integer representing the number of logs to generate. if 0, it will generate logs indefinitely.

    Methods:
        generate_logs: Generates logs based on specified parameters.
        generate_log_entry: Generates a log entry.
        generate_log: Generates a single log entry.
    """
    def __init__(self, log_file: str = 'sample.log', num_logs: int = 10):
        self.levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING', 'CRITICAL', 'FATAL']
        self.messages = [
            "Application started",
            "Connection timeout",
            "Database connection failed",
            "User logged in",
            "Processing data",
            "Data saved successfully",
            "Low disk space",
            "Server crashed",
            "Server restarted",
            "Application stopped",
            "Invalid request",
            "User logged out",
            "Data processing failed",
        ]
        self.log_file = log_file
        self.num_logs = num_logs

    def generate_logs(self):
        """
        Generates logs based on specified parameters.
        """
        if self.num_logs == 0:
            while True:
                self.generate_log()
                time.sleep(random.uniform(1, 5))
        else:
            for _ in range(self.num_logs):
                self.generate_log()
                time.sleep(random.uniform(1, 5))
    
    def generate_log(self):
        """
        Generates a single log entry.
        """
        level = random.choice(self.levels)
        message = random.choice(self.messages)
        log_entry = self.generate_log_entry(level, message)
        with open(self.log_file, 'a') as f:
            f.write(log_entry)

    def generate_log_entry(self, level: str, message: str) -> str:
        """
        Generates a log entry with specified level and message.

        Args:
            level (str): The log level.
            message (str): The log message.
        """
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        return f"{timestamp} - {level}: {message}\n"
    
if __name__ == '__main__':
    num_logs = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    logs = GenerateLogs(num_logs=num_logs)
    try:
        logs.generate_logs()
    except KeyboardInterrupt:
        print("Logs generation stopped by user.")