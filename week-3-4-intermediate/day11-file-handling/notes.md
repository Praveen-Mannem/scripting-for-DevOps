# Day 11: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **File reading**: open() with 'r' mode
2. **File writing**: open() with 'w' mode (overwrites)
3. **File appending**: open() with 'a' mode
4. **with statement**: Automatically closes files
5. **File paths**: os.path module

## File Handling Cheatsheet
```python
# Read entire file
with open('file.txt', 'r') as file:
    content = file.read()

# Read line by line
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read all lines
with open('file.txt', 'r') as file:
    lines = file.readlines()

# Write to file (overwrites)
with open('file.txt', 'w') as file:
    file.write("content\n")

# Append to file
with open('file.txt', 'a') as file:
    file.write("more content\n")

# Check if file exists
import os
if os.path.exists('file.txt'):
    print("exists")

# Get file size
size = os.path.getsize('file.txt')
```

## DevOps Use Cases
- **Log analysis**: Read and parse log files
- **Configuration**: Read/write config files
- **Backups**: Create file backups
- **Reports**: Generate text reports

## Practice Summary
- [ ] Completed log_reader.py
- [ ] Completed config_writer.py
- [ ] Completed backup_creator.py

## Tomorrow's Preview
Day 12: Error Handling - Handle exceptions gracefully
