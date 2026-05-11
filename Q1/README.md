
---

## Features

- Parses log files line by line
- Filters logs by type (error/warning/info/debug)
- Displays most recent logs first
- Default behavior:
  - Log type = `error`
  - Lines = `10`
- Handles invalid inputs and file errors

---

## Project Structure
```
Q1/
│
├── LogParser.java              # Main Java file (contains logic for log parsing)
├── LogParser.class             # Compiled Java file
├── LogParser.log               # Sample log input file
├── log_parsing_Question.txt    # Problem statement
├── LogParser_outcome.png       # Output screenshot
└── README.md                   # Documentation file
```
---

## How to Compile

Open terminal inside `Q1` folder and run:

```bash id="run1"
javac LogParser.java
```

---

## How to Run

```bash id="run2"
java LogParser LogParser.log 10 error,warning
```

---

## Input Parameters

```text id="input"
1. File path (required)
2. Number of lines (optional, default = 10)
3. Log types (optional, default = error)
```

---

## Example Run

```bash id="ex1"
java LogParser LogParser.log 15 info,debug
```

---

## Concepts Used

- File Handling in Java
- String Parsing
- Exception Handling
- Command Line Arguments
- Filtering Logic

---
