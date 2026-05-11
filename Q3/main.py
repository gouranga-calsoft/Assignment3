import platform
from hosts.windows_host import WindowsHost
from hosts.linux_host import LinuxHost


def main():
    os_type = platform.system()

    if os_type == "Windows":
        host = WindowsHost()
    elif os_type == "Linux":
        host = LinuxHost()
    else:
        print(f"Unsupported operating system: {os_type}")
        return

    # Collect hardware information
    host.get_hardware_info()

    # Display in JSON format
    host.display_hardware_info()


if __name__ == "__main__":
    main()