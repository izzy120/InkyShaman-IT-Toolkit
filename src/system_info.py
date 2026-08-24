import platform
import psutil

def get_system_info():
    system_info = {
        "Computer Name": platform.node(),
        "User Name": psutil.users()[0].name,
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()[0],
        "CPU Cores": psutil.cpu_count(logical=False),
        "CPU Threads": psutil.cpu_count(logical=True),
        "CPU Frequency": f"{psutil.cpu_freq().current:.2f} MHz",
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
        "RAM": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        "disk space": f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB",
        "disk space used": f"{psutil.disk_usage('/').used / (1024 ** 3):.2f} GB",
        "disk space free": f"{psutil.disk_usage('/').free / (1024 ** 3):.2f} GB",
        "python Version": platform.python_version()
    }
    return system_info
