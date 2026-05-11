# Log File Parsing

## Overview

This project is a Java-based Log File Parsing System that reads and filters log entries from a log file based on user-defined log types such as:

- error
- warning
- info
- debug

The program efficiently parses log files and displays the most recent matching log entries by reading the file from the end. The implementation follows clean programming practices with proper exception handling and optimized parsing logic.

---

## Problem Statement

Given a log file, write a program to parse the file based on log types to be displayed.

The supported log types are:

- error
- warning
- info
- debug

The program should display the most recent filtered logs based on line numbers.

---

## Input Parameters

### 1. File Path

Path of the log file to parse.

Example:

```bash
LogParser.log
```

---

### 2. Number of Lines to Display (Optional)

- Default value: `10`
- Determines how many matching log entries should be displayed.

---

### 3. Log Types to Display (Optional)

- Default value: `error`
- Multiple log types can be passed as comma-separated values.

Example:

```bash
error,warning
```

---

## Features

- Parses log files efficiently
- Supports multiple log types
- Displays most recent matching logs
- Reads log file from the end for optimization
- Handles invalid file paths
- Handles invalid log types
- Uses clean and modular Java code
- Supports optional command-line parameters

---

## Project Structure

```bash
Q1/
│
├── log_parsing_Question.txt      # Assignment problem statement
├── LogParser_outcome.png         # Sample output screenshot
├── LogParser.class               # Compiled Java bytecode
├── LogParser.java                # Main Java source file
├── LogParser.log                 # Sample log file
└── README.md                     # Project documentation
```

---

## Technologies Used

- Java
- File Handling
- Exception Handling
- Collections Framework
- String Processing
- Command-Line Arguments

---

## Core Concepts Used

### File Handling

The program reads log entries from a text-based log file.

---

### Exception Handling

The program raises exceptions for:

- Invalid file path
- Invalid log type
- File reading errors

Example:

```java
throw new IllegalArgumentException("Invalid log type");
```

---

### String Processing

Each log line is parsed and filtered using string operations.

Supported log keywords:

- error
- warning
- info
- debug

---

### Reverse File Parsing Optimization

The program is optimized to fetch the latest matching logs efficiently by:

- Reading logs from the end of the file
- Stopping once required matching entries are found
- Avoiding unnecessary full-file traversal

This improves performance for large log files.

---

## How the Program Works

1. Accepts user input parameters
2. Validates file path
3. Validates log types
4. Reads log file from the end
5. Filters matching log entries
6. Displays most recent logs

---

## Compilation Instructions

### Step 1: Navigate to Project Directory

```bash
cd Q1
```

---

### Step 2: Compile the Program

```bash
javac LogParser.java
```

This generates:

```bash
LogParser.class
```

---

## Running the Program

### Basic Execution

```bash
java LogParser
```

Uses default values:

- Number of lines = 10
- Log type = error

---

### Run with File Path

```bash
java LogParser LogParser.log
```

---

### Run with File Path and Number of Lines

```bash
java LogParser LogParser.log 5
```

---

### Run with All Parameters

```bash
java LogParser LogParser.log 10 info,debug
```

---

## Example Output

```text
java LogParser LogParser.log 3 info,error
[INFO] 2019-10-17 11:42:40 root() : End parsing the plugin vrops
[ERROR] 2019-10-17 11:42:40 util.smtp_server() : Error: unable to send email (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials v3sm1080198pfn.18 - gsmtp')
[INFO] 2019-10-17 11:42:36 root() : creation_table_list : [['89f99dbd-1a01-463b-90ad-5725dd65b2a8', 'INC0010433', 'Virtual machine disk I/O write latency is high'], ['81f2770b-d276-4a21-9c00-c0df7b9134dd', 'INC0010434', 'Virtual machine disk I/O write latency is high'], ['a66ff580-5316-4959-bc6d-48fc756a77fb', 'INC0010435', 'Virtual machine disk I/O write latency is high'], ['4efc5055-f823-4636-b8c9-fa561d6c5e4e', 'INC0010436', 'License will expire soon']]
```

---

## Assignment Requirements Covered

- File parsing
- Filtering by log type
- Optional command-line parameters
- Exception handling
- Reverse log traversal optimization
- Most recent log extraction
- Java-based implementation

---
