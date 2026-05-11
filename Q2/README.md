# Inventory Filter System (C++)

## Overview

This project is a **C++ based Inventory Filtering System** that reads inventory data from a JSON file and filters it based on user-defined criteria such as **CPU usage, Memory usage, or OS type (Linux/Windows)**.

The project is built using **Object-Oriented Programming (OOP)** principles and is optimized for handling large datasets efficiently.

---

## Problem Statement

Given a JSON file containing inventory information, the program filters the data based on the following criteria:

### Filter Criteria

- **CPU** → Displays the item with maximum CPU usage
- **Memory** → Displays the item with maximum Memory usage
- **Linux** → Displays all Linux-based systems
- **Windows** → Displays all Windows-based systems

---

## Features

- Reads inventory data from `inventory.json`
- Filters based on CPU, Memory, or OS type
- Handles invalid or missing filter criteria using exceptions
- Object-Oriented Design (OOP)
- Optimized for large file processing
- Easy to compile and run on Windows

---

## Project Structure

```bash
Q2/
│
├── inventory_filter.cpp          # Main source file (entry point)
├── inventory_filter.exe          # Compiled executable
├── inventory.json                # Input JSON file
├── inventory_info_Question.txt   # Problem statement
├── inventory_outcome.png         # Sample output screenshot
└── README.md                     # Project documentation
```

---

# Technologies Used

- C++
- STL (Standard Template Library)
- JSON Parsing
- Object-Oriented Programming (OOP)

---

# Concepts Used

## Object-Oriented Programming (OOP)

The project follows OOP principles such as:

- **Classes & Objects** → Used for inventory management and filtering
- **Encapsulation** → Data and related methods grouped together
- **Abstraction** → Hides implementation details from users
- **Modular Design** → Separate logic for parsing, filtering, and displaying data

---

## Exception Handling

The program throws exceptions in the following cases:

- Missing filter criteria
- Invalid filter criteria
- File reading/parsing errors

Example:

```cpp
throw invalid_argument("Invalid filter criteria");
```

---

## JSON File Processing

The inventory data is read from a JSON file and parsed into C++ objects for filtering operations.

---

# Input

The program accepts one filter criterion:

```text
CPU
Memory
Linux
Windows
```

---

# Output

---


# How to Compile and Run (Windows)

## Using g++ (MinGW)

### Step 1: Open Command Prompt

Navigate to the project directory

---

### Step 2: Compile the Program

```bash
g++ inventory_filter.cpp -o inventory_filter.exe
```

---

### Step 3: Run the Executable

```
.\inventory_filter.exe one_criteria
```

---

## Sample Run

```bash
.\inventory_filter.exe CPU
```
```bash
.\inventory_filter.exe Memory
```
```bash
.\inventory_filter.exe Linux
```
```bash
.\inventory_filter.exe Windows
```

# Assignment Requirements Covered

JSON file processing  
Filtering by CPU/Memory/OS  
Exception handling  
Object-Oriented Design  
Large file optimization  

---


