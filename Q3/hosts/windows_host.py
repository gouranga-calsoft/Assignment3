# hosts/windows_host.py

import socket
import platform
import shutil
import ctypes

from hosts.host_info import HostInfo


class WindowsHost(HostInfo):
    def get_hardware_info(self):
        # ---------------------------------------------------------
        # Hostname
        # ---------------------------------------------------------
        self.hostname = socket.gethostname()

        # ---------------------------------------------------------
        # CPU Information
        # platform.processor() returns CPU details on Windows
        # Example:
        # "Intel64 Family 6 Model 140 Stepping 1, GenuineIntel"
        # ---------------------------------------------------------
        try:
            self.cpu = platform.processor()
            if not self.cpu:
                self.cpu = "Unknown"
        except Exception:
            self.cpu = "Unknown"

        # ---------------------------------------------------------
        # Memory Information (Total Physical RAM)
        # Uses Windows API through ctypes
        # ---------------------------------------------------------
        try:
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            memory_status = MEMORYSTATUSEX()
            memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)

            ctypes.windll.kernel32.GlobalMemoryStatusEx(
                ctypes.byref(memory_status)
            )

            total_memory_bytes = memory_status.ullTotalPhys
            self.memory = f"{total_memory_bytes / (1024 ** 3):.2f} GB"

        except Exception:
            self.memory = "Unknown"

        # ---------------------------------------------------------
        # Disk Size (Current Drive Total Capacity)
        # ---------------------------------------------------------
        try:
            total, used, free = shutil.disk_usage("C:\\")
            self.disk_size = f"{total / (1024 ** 3):.2f} GB"
        except Exception:
            self.disk_size = "Unknown"

        # ---------------------------------------------------------
        # IP Address
        # Uses the common method defined in HostInfo
        # ---------------------------------------------------------
        self.ip = self.get_ip_address()