import psutil
import time
from datetime import datetime
import logging

CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 80
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def monitor_cpu():
    print("=" * 40)
    print("       SYSTEM HEALTH MONITOR")

    print("=" * 40)
    print("Monitoring CPU usage...")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent
            current_time = datetime.now().strftime("%H:%M:%S")

            print(f"[{current_time}] CPU Usage: {cpu_usage}%")
            print(f"[{current_time}] RAM Usage: {memory_usage}%")
            print(f"[{current_time}] Disk Usage: {disk_usage}%")
            logging.info(
                f"CPU: {cpu_usage}% | RAM: {memory_usage}% | Disk: {disk_usage}%"
            )
            if cpu_usage >= CPU_THRESHOLD:
                print("WARNING: High CPU usage!")
                logging.warning("High CPU usage detected: %s%%", cpu_usage)

               
 
               
  

            if memory_usage >= RAM_THRESHOLD:
                print("WARNING: High RAM usage!")
                logging.warning("High RAM usage detected: %s%%", memory_usage) 

            if disk_usage >= DISK_THRESHOLD:
                print("WARNING: High disk usage!")
                logging.warning("High disk usage detected: %s%%", disk_usage) 

               

    


            if cpu_usage >= CPU_THRESHOLD:
                print("WARNING: High CPU usage detected!")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    monitor_cpu()