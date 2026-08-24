import socket
import subprocess
import urllib.request


def get_network_info():
    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        local_ip = "Unable to determine"

    return {
        "Hostname": hostname,
        "Local IP": local_ip
    }

def get_external_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org", timeout=5) as response:
            return response.read().decode("utf-8")
    except Exception:
        return "Unable to determine"

def test_internet_connection():
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"],
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        return False

