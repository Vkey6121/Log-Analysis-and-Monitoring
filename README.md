# Log Analysis and Monitoring Script v1.0

This project is a log analysis and monitoring script that helps analyze and monitor log files. 
This project provides monitoring and analysis capabilities for log files.<br>
*With Logger Support*

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


## Generating Logs

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

2. Follow the prompts to specify the log file name and the number of logs to generate.