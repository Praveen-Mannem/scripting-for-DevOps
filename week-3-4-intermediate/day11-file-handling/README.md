# Day 11: File Handling - Reading and Writing Files

## 📚 Learning Objectives
- Read from files
- Write to files
- Append to files
- Work with file paths
- Handle file operations safely

## 🎯 Why This Matters for DevOps
File operations are critical for:
- Reading configuration files
- Processing log files
- Writing reports
- Creating backups
- Managing system files

---

## 📖 Concepts

### 1. Reading Files
```python
# Read entire file
with open('server.log', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('server.log', 'r') as file:
    for line in file:
        print(line.strip())

# Read all lines into a list
with open('server.log', 'r') as file:
    lines = file.readlines()
```

### 2. Writing Files
```python
# Write to file (overwrites)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Append to file
with open('output.txt', 'a') as file:
    file.write("Appended line\n")
```

### 3. File Modes
```python
'r'  # Read (default)
'w'  # Write (overwrites)
'a'  # Append
'r+' # Read and write
'x'  # Create (fails if exists)
```

### 4. Working with Paths
```python
import os

# Check if file exists
if os.path.exists('config.txt'):
    print("File exists")

# Get file size
size = os.path.getsize('config.txt')

# Join paths
path = os.path.join('logs', 'server.log')
```

---

## 💻 Practice Exercises

### Exercise 1: Log File Reader
**File:** `log_reader.py`

### Exercise 2: Configuration File Writer
**File:** `config_writer.py`

### Exercise 3: Backup Creator
**File:** `backup_creator.py`

---

## ⏭️ Next Steps
Tomorrow: Day 12 - Error Handling (try/except)
