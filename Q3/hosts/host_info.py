from abc import ABC, abstractmethod
import json
import socket


class HostInfo(ABC):
    def __init__(self):
        # Common attributes for all hosts
        self.hostname = ""
        self.memory = ""
        self.cpu = ""
        self.ip = ""
        self.disk_size = ""

    @abstractmethod
    def get_hardware_info(self):
        """
        Abstract method.
        Each child class must implement its own logic to collect
        hardware information.
        """
        pass

    def get_ip_address(self):
        """
        Returns the primary IP address of the system.
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # No actual connection is made; this helps determine
            # the preferred outbound IP.
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "Unknown"

    def display_hardware_info(self):
        """
        Displays all collected hardware information in JSON format.
        """
        data = {
            "hostname": self.hostname,
            "memory": self.memory,
            "cpu": self.cpu,
            "ip": self.ip,
            "disk_size": self.disk_size
        }

        print(json.dumps(data, indent=4))