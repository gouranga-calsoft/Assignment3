# Get Hardware Info

## Overview

This project is a Python-based Hardware Information System that retrieves real-time hardware details of the machine on which the program is executed.

The application follows an Object-Oriented Programming (OOP) approach using inheritance, abstraction, and modular design. Based on the operating system, the program dynamically creates either a LinuxHost or WindowsHost object to fetch and display system hardware information in JSON format.

The project is structured using Python packages and modules for better maintainability and scalability.

---

## Problem Statement

Write a program to display real-time hardware information of the system.

Requirements:

- Use Object-Oriented Programming concepts
- Use Python package/module structure
- Create a parent class `HostInfo`
- Create child classes `LinuxHost` and `WindowsHost`
- Include the following attributes:
  - hostname
  - memory
  - cpu
  - ip
  - disk_size
- Implement an abstract method `get_hardware_info()`
- Display hardware information in JSON format
- Instantiate the appropriate class based on the OS type

---

## Features

- Detects operating system automatically
- Retrieves real-time hardware information
- Displays hardware details in JSON format
- Uses abstract classes and inheritance
- Modular package-based structure
- Cross-platform implementation for Linux and Windows
- Easy to extend for additional operating systems

---

## Project Structure

```bash
Q3/
│
├── hosts/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── host_info.py
│   ├── linux_host.py
│   └── windows_host.py
│
├── get_hardware_info_Question.txt
├── main.py
├── Output.png
└── README.md
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Abstract Base Classes (ABC)
- JSON
- OS/System Commands
- Python Modules and Packages

---

## OOP Concepts Used

### 1. Abstraction

The `HostInfo` class defines an abstract method:

```python
get_hardware_info()
```

This method is implemented differently by each child class depending on the operating system.

---

### 2. Inheritance

The following classes inherit from `HostInfo`:

- `LinuxHost`
- `WindowsHost`

This allows code reuse and platform-specific implementation.

---

### 3. Encapsulation

Hardware-related attributes and methods are encapsulated inside classes.

Example attributes:

- hostname
- memory
- cpu
- ip
- disk_size

---

### 4. Polymorphism

Both LinuxHost and WindowsHost implement the same method:

```python
get_hardware_info()
```

but with OS-specific logic.

---

## Sample Output

```json
{
    "hostname": "DESKTOP-ABC123",
    "cpu": "Intel(R) Core(TM) i7",
    "memory": "16 GB",
    "ip": "192.168.1.10",
    "disk_size": "512 GB"
}
```

---

## How to Run

### Step 3: Run the Program

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## OS Detection Logic

The program uses Python's `platform` module to detect the operating system.

Example:

```python
platform.system()
```

Based on the result:

- Windows → `WindowsHost`
- Linux → `LinuxHost`

---

## Exception Handling

The project handles:

- Unsupported operating systems
- Command execution failures
- Missing system commands
- Runtime exceptions

Example:

```python
raise Exception("Unsupported Operating System")
```

---

## Design Advantages

- Clean modular architecture
- Easy to maintain
- Easy to extend
- Platform-independent structure
- Reusable base class design

---

## Assignment Requirements Covered

- Object-Oriented Programming
- Abstract Classes
- Inheritance
- Python Packages and Modules
- OS-based Class Instantiation
- Real-Time Hardware Information
- JSON Output Format

---
