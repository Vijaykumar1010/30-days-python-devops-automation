
import psutil

def system_health():

    # CPU usage
    cpu = psutil.cpu_percent(interval=1)

    # Memory usage
    memory = psutil.virtual_memory().percent

    # Disk usage
    disk = psutil.disk_usage('/').percent

    print("===== SYSTEM HEALTH REPORT =====")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    if cpu > 80 or memory > 80 or disk > 80:
        print("Status: WARNING - High resource usage")
    else:
        print("Status: HEALTHY")

system_health()
