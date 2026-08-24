# ============================================================
# INKYSHAMAN IT TOOLKIT
# hardware_info.py
# ============================================================

# TYPE: Module Imports
# These libraries give us access to hardware and operating
# system information.
import platform
import psutil
import subprocess


# ============================================================
# FUNCTION: get_hardware_info
# TYPE: Function
# PURPOSE: Collect hardware information from the computer.
# ============================================================

# ============================================================
# GPU DETECTION
# TYPE: Variable + System Command
# PURPOSE: Ask Windows for the installed GPU name.
# ============================================================

gpu_result = subprocess.run(
    [
        "powershell",
        "-Command",
        "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
    ],
    capture_output=True,
    text=True
)

gpu_name = gpu_result.stdout.strip()

def get_hardware_info():

    # TYPE: Dictionary
    # This dictionary stores all of the hardware information
    # we collect so the rest of the program can use it.
    hardware_info = {
        # TYPE: String / Function Call
        # Gets the CPU/processor name.
        "CPU": platform.processor(),

        "GPU": gpu_name,

        # TYPE: Integer / Function Call
        # Gets the number of physical CPU cores.
        "CPU Cores": psutil.cpu_count(logical=False),

        # TYPE: Integer / Function Call
        # Gets the total number of logical CPU threads.
        "CPU Threads": psutil.cpu_count(logical=True),

        # TYPE: Float / Function Call
        # Gets the current CPU usage percentage.
        "CPU Usage": psutil.cpu_percent(interval=1),

        # TYPE: Float / Calculation
        # Gets the amount of RAM installed in GB.
        "RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2),

        # TYPE: Float / Function Call
        # Gets the current RAM usage percentage.
        "RAM Usage": psutil.virtual_memory().percent,

        # TYPE: Float / Calculation
        # Gets the total size of the C: drive in GB.
        "Storage Total": round(
            psutil.disk_usage("C:\\").total / (1024 ** 3), 2
        ),

        # TYPE: Float / Calculation
        # Gets how much space is currently being used.
        "Storage Used": round(
            psutil.disk_usage("C:\\").used / (1024 ** 3), 2
        ),

        # TYPE: Float / Calculation
        # Gets how much free space remains.
        "Storage Free": round(
            psutil.disk_usage("C:\\").free / (1024 ** 3), 2
        ),

        # TYPE: String / Function Call
        # Gets the operating system name.
        "Operating System": platform.system(),

        # TYPE: String / Function Call
        # Gets the OS version.
        "OS Version": platform.version(),

        # TYPE: String / Function Call
        # Gets whether Windows is 32-bit or 64-bit.
        "Architecture": platform.architecture()[0],
    }

    # TYPE: Return Statement
    # Sends the dictionary back to whatever part of the
    # program called this function.
    return hardware_info


# ============================================================
# FUNCTION: show_hardware_info
# TYPE: Function
# PURPOSE: Display the collected hardware information.
# ============================================================

def show_hardware_info():

    # Call our hardware information function.
    info = get_hardware_info()

    print("\n" + "=" * 50)
    print("              HARDWARE DIAGNOSTICS")
    print("=" * 50)

    # TYPE: For Loop
    # Goes through every key/value pair in our dictionary.
    for key, value in info.items():
        print(f"{key}: {value}")

    print("=" * 50)
    input("\nPress Enter to return to the main menu...")