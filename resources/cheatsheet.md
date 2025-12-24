# Python Cheat Sheet for DevOps

Quick reference guide for Python syntax and common DevOps operations.

---

## Basic Syntax

### Print Statement
```python
print("Hello")
print(f"Value: {variable}")  # f-string
```

### Comments
```python
# Single line comment
"""
Multi-line comment
or docstring
"""
```

### Variables
```python
name = "server-1"
count = 10
price = 99.99
is_active = True
```

---

## Data Types

### Strings
```python
text = "Hello"
text = 'Hello'
text = f"Hello {name}"  # f-string

# Methods
text.upper()        # HELLO
text.lower()        # hello
text.strip()        # Remove whitespace
text.split(",")     # Split into list
text.replace("a", "b")
```

### Numbers
```python
# Integer
count = 10

# Float
price = 99.99

# Operations
+ - * / // % **
```

### Lists
```python
servers = ["web-1", "db-1", "app-1"]

servers[0]          # Access: web-1
servers.append("cache-1")
servers.remove("db-1")
servers.pop()       # Remove last
len(servers)        # Length
```

### Dictionaries
```python
server = {
    "name": "web-1",
    "ip": "192.168.1.10",
    "cpu": 45
}

server["name"]      # Access
server["memory"] = 60  # Add
del server["cpu"]   # Delete
server.keys()       # All keys
server.values()     # All values
```

---

## Control Flow

### If-Else
```python
if cpu > 80:
    print("High")
elif cpu > 50:
    print("Medium")
else:
    print("Low")
```

### For Loop
```python
for server in servers:
    print(server)

for i in range(10):
    print(i)
```

### While Loop
```python
while count > 0:
    print(count)
    count -= 1
```

---

## Functions

### Basic Function
```python
def greet(name):
    return f"Hello {name}"

result = greet("Praveen")
```

### Default Arguments
```python
def connect(host, port=22):
    print(f"Connecting to {host}:{port}")
```

### Multiple Returns
```python
def get_stats():
    return cpu, memory, disk

c, m, d = get_stats()
```

---

## File Operations

### Read File
```python
with open("file.txt", "r") as f:
    content = f.read()

# Line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Write File
```python
with open("file.txt", "w") as f:
    f.write("Hello\n")
```

### Append File
```python
with open("file.txt", "a") as f:
    f.write("New line\n")
```

---

## JSON Operations

```python
import json

# Write JSON
data = {"name": "server-1", "cpu": 45}
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("config.json", "r") as f:
    data = json.load(f)
```

---

## Date and Time

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Time difference
delta = timedelta(days=1, hours=2)
future = now + delta

# Parse string
dt = datetime.strptime("2024-12-24", "%Y-%m-%d")
```

---

## System Commands

```python
import subprocess

# Run command
result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.returncode)  # 0 = success
```

---

## Working with APIs

```python
import requests

# GET request
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()

# POST request
data = {"key": "value"}
response = requests.post(
    "https://api.example.com/create",
    json=data,
    headers={"Authorization": "Bearer token"}
)
```

---

## Environment Variables

```python
import os

# Read
api_key = os.getenv("API_KEY", "default")

# Set
os.environ["MY_VAR"] = "value"

# With .env file
from dotenv import load_dotenv
load_dotenv()
```

---

## Error Handling

```python
try:
    result = risky_operation()
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print(f"Invalid value: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always runs")
```

---

## Command Line Arguments

```python
import argparse

parser = argparse.ArgumentParser(description='My script')
parser.add_argument('name', help='Server name')
parser.add_argument('--port', type=int, default=22)
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()
print(args.name, args.port)
```

---

## Common DevOps Patterns

### Check Server Health
```python
def check_health(cpu, memory, disk):
    if cpu > 80 or memory > 80 or disk > 80:
        return "CRITICAL"
    elif cpu > 60 or memory > 60 or disk > 60:
        return "WARNING"
    return "OK"
```

### Parse Log Line
```python
def parse_log(line):
    parts = line.split(" - ")
    return {
        "timestamp": parts[0],
        "level": parts[1],
        "message": parts[2]
    }
```

### Retry Logic
```python
import time

def retry(func, max_attempts=3, delay=1):
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            time.sleep(delay)
```

---

## Useful Libraries

### System Monitoring
```python
import psutil

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
```

### Path Operations
```python
from pathlib import Path

path = Path("/path/to/file")
path.exists()
path.is_file()
path.is_dir()
path.read_text()
path.write_text("content")
```

### Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

---

## Quick Tips

### List Comprehension
```python
# Instead of:
squares = []
for x in range(10):
    squares.append(x**2)

# Use:
squares = [x**2 for x in range(10)]
```

### Dictionary Comprehension
```python
servers = {f"server-{i}": i for i in range(5)}
```

### Multiple Assignment
```python
a, b, c = 1, 2, 3
```

### String Formatting
```python
name = "server-1"
cpu = 75

# f-string (recommended)
msg = f"{name}: CPU {cpu}%"

# format()
msg = "{}: CPU {}%".format(name, cpu)

# % operator (old)
msg = "%s: CPU %d%%" % (name, cpu)
```

---

**Keep this handy while coding! 📚**
