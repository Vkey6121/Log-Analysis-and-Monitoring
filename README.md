# Log Analysis and Monitoring Script

This project is a log analysis and monitoring script that helps analyze and monitor log files. 

# Prerequisites
Python 3.x

# Dependencies
It uses the following built-in Python modules:

logging: For logging and log file handling.

time: For introducing delays in the monitoring loop.

random: For randomly selecting log levels.

re: For regular expression pattern matching to detect HTTP status codes.

argparse: For parsing command-line arguments.

configparser: For reading configuration settings from a file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BANZOM/Log-Analysis-and-Monitoring-Script.git
    ```

2. Change to the project directory:

    ```bash
    cd Log-Analysis-and-Monitoring-Script
    ```

## Usage

1. Run the script:

    ```bash
    python log_monitor.py /path/to/log/file.log
    # Press Ctrl+C to stop monitoring logs, then you'll get the overall summary
    ```

2. Follow the prompts to specify the log file and the analysis options.


## Implementing Log File Monitoring

To generate logs for testing purposes, you can use the `generate_logs.py` file included in the project. 

1. Run the script:

    ```bash
    # To generate a specific number of logs
    python generate_logs.py <number_of_logs>
    # Press Ctrl+C to stop generating logs
    ```

    or

    ```bash
    # To generate infinite logs
    python generate_logs.py
    # Press Ctrl+C to stop generating logs
    ```
    
