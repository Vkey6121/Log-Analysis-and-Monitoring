import os
import time
import sys
from collections import Counter
import logging

class LogMonitor:
    """
    A class to monitor logs

    Attributes:
        log_file: A string representing the log file path.
    
    Methods:
        monitor_logs: Monitors logs for new entries.
        analyze_log_entry: Analyzes a log entry for error messages, failures, HTTP status codes, etc.
        generate_report: Generates a report of log analysis.
    """
    def __init__(self, log_file: str = 'sample.log'):
        self.log_file = log_file
        self.log_analysis = Counter()
        self.error_messages = Counter()

        # Set up logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        log_file_name = f"log_monitor_{time.strftime('%Y%m%d%H%M%S')}.log" # Log file name with timestamp
        handler = logging.FileHandler(log_file_name)
        handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)
    
    def monitor_logs(self):
        """
        Monitors logs for new entries.
        """
        try:
            with open(self.log_file, 'r') as f:
                f.seek(0, os.SEEK_END)
                while True:
                    line = f.readline()
                    if line:
                        self.logger.info(line.rstrip())
                        print(line.rstrip())
                        self.analyze_log_entry(line)
                    else:
                        time.sleep(1)
        except FileNotFoundError:
            self.logger.error(f"Log file '{self.log_file}' not found.")
            print(f"Log file '{self.log_file}' not found.")
            return
        except KeyboardInterrupt:
            self.logger.info("Log monitoring stopped.")
            print("\nLog monitoring stopped.")
            return
        
    def analyze_log_entry(self, log_entry: str):
        """
        Analyzes a log entry for error messages, failures, HTTP status codes, etc.
        """
        error_keywords = ['error', 'fail', 'exception', 'warning', 'fatal', 'critical']
        http_status_codes = [str(code) for code in range(400, 600)]
        
        error_count = sum(keyword in log_entry.lower() for keyword in error_keywords)
        http_error_count = sum(status_code in log_entry for status_code in http_status_codes)

        self.log_analysis.update({'errors': error_count, 'http_errors': http_error_count})

        # Store error messages and count occurrences
        if error_count > 0 or http_error_count > 0:
            error_message = log_entry.split(':')[-1].strip()
            self.error_messages[error_message] += 1

        self.logger.info(f"Log entry analyzed: {log_entry}")

    def generate_report(self):
        """
        Generates a report of log analysis.
        """
        print("-------------------")
        print("Log Analysis Report")
        print("-------------------")
        self.logger.info("Log Analysis Report")

        for key, value in self.log_analysis.items():
            print(f"{key.capitalize()}: {value}")
            self.logger.info(f"{key.capitalize()}: {value}")

        print("-------------------")  
        print("Top 5 Error Messages")
        print("-------------------")

        self.logger.info("Top 5 Error Messages")
        for error_message, count in self.error_messages.most_common(5):
            self.logger.info(f"{error_message}: {count}")
            print(f"{error_message}: {count}")

        print("-------------------")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
        log_monitor = LogMonitor(log_file)
    else:
        log_monitor = LogMonitor()

    log_monitor.monitor_logs()
    log_monitor.generate_report()
