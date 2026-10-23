# System Health Monitor

## Overview

System Health Monitor is a Python-based monitoring tool that tracks CPU usage, memory consumption, and disk usage. It displays system resource measurements in the terminal, records monitoring information in a log file, and generates warnings when resource usage reaches configured thresholds.

This project demonstrates practical Linux, Python, logging, and version control skills relevant to DevOps engineering.

## Features

* Real-time CPU usage monitoring
* RAM usage monitoring
* Disk usage monitoring
* Configurable resource usage thresholds
* Timestamped logging
* Warnings when resource usage exceeds configured thresholds
* Linux and Ubuntu environment support

## Technologies Used

* Python 3
* psutil
* Linux / Ubuntu
* Python logging module
* Git and GitHub

## Prerequisites

Before running the project, ensure you have:

* Python 3 installed
* pip installed
* Git installed
* Linux, Ubuntu, or WSL with Ubuntu
* Access to a terminal

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sandrastanali/system_health_monitor.git
cd system_health_monitor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux or Ubuntu:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python3 -m pip install psutil
```

## Usage

Run the monitoring program:

```bash
python3 cpu_monitor.py
```

The program monitors system resource usage and displays measurements in the terminal.

Press `Ctrl+C` to stop monitoring.

## Logging

The monitoring program records system resource measurements and may generate warnings when resource usage exceeds configured thresholds.

The log filename and location depend on the logging configuration in the project.

## Project Structure

| File                | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `README.md`         | Project documentation and usage instructions                 |
| `cpu_monitor.py`    | Python-based system monitoring                               |
| `monitor.conf`      | Monitoring configuration                                     |
| `system_monitor.sh` | Bash-based system monitoring                                 |
| `parse_logs.sh`     | Log parsing and analysis                                     |
| `calms_summary.md`  | Summary of the CALMS framework and its application to DevOps |

## Learning Objectives

This project provides practical experience with:

* Python scripting and system monitoring
* Linux command-line operations
* Resource measurement and logging
* Configuration management
* Git branching and version control
* GitHub collaboration and Pull Requests
* DevOps principles and automation

## Future Improvements

Possible enhancements include:

* Automated testing
* Continuous integration with GitHub Actions
* Improved error handling
* Automated monitoring schedules
* More detailed monitoring reports
* Notifications when resource usage exceeds configured thresholds

## Author

Developed as a learning project to practise system administration, Python programming, and DevOps engineering.
