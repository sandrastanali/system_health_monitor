# System Health Monitor

## Overview

A Python-based system monitoring tool that tracks CPU usage, RAM usage, and disk usage. It displays measurements in the terminal, records them in a log file, and generates warnings when resource usage reaches configured thresholds.

## Features

* Real-time CPU usage monitoring
* RAM usage monitoring
* Disk usage monitoring
* Configurable resource usage thresholds
* Timestamped logging
* Warnings for high resource usage

## Technologies Used

* Python 3
* psutil
* Linux / Ubuntu
* Python logging module
* Git and GitHub (for version control and project hosting)

## Requirements

* Python 3
* pip
* A Linux environment or WSL Ubuntu
* psutil

## Installation

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd system-health-monitor
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependency:

```bash
python3 -m pip install psutil
```

## Usage

Run the monitoring script:

```bash
python3 cpu_monitor.py
```

Press `Ctrl+C` to stop monitoring.

## Logging

The program records CPU, RAM, and disk usage in `system_health.log`, including timestamps and warning messages when configured thresholds are exceeded.

## Learning Objectives

This project demonstrates introductory Python scripting, Linux command-line usage, system resource monitoring, logging, and automation concepts relevant to DevOps.
