import subprocess
import socket
from hosts.host_info import HostInfo


class LinuxHost(HostInfo):
    def get_hardware_info(self):

        # Default values
        self.hostname = socket.gethostname()
        self.cpu = "Unknown"
        self.memory = "Unknown"
        self.disk_size = "Unknown"

        # CPU
        try:
            output = subprocess.check_output("lscpu", shell=True, text=True)
            for line in output.splitlines():
                if "Model name:" in line:
                    self.cpu = line.split(":", 1)[1].strip()
                    break
        except Exception:
            pass

        # Memory
        try:
            output = subprocess.check_output("free -h", shell=True, text=True)
            for line in output.splitlines():
                if "Mem:" in line:
                    parts = line.split()
                    self.memory = parts[1] if len(parts) > 1 else "Unknown"
                    break
        except Exception:
            pass

        # Disk
        try:
            output = subprocess.check_output("df -h /", shell=True, text=True)
            lines = output.splitlines()
            if len(lines) > 1:
                parts = lines[1].split()
                self.disk_size = parts[1] if len(parts) > 1 else "Unknown"
        except Exception:
            pass

        # IP
        self.ip = self.get_ip_address()