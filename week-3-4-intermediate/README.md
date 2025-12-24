# Week 3-4: Intermediate Python for DevOps

Complete learning materials for intermediate Python concepts essential for DevOps automation.

## Overview

This week builds on Week 1-2 fundamentals and introduces:
- File operations (reading/writing logs and configs)
- Error handling (making scripts robust)
- JSON parsing (working with APIs and configs)
- Date/time operations (timestamps and scheduling)
- Command-line arguments (flexible scripts)

---

## Daily Breakdown

### Day 11-12: File Operations

**Topics:**
- Reading files (`open()`, `read()`, `readlines()`)
- Writing files (`write()`, `writelines()`)
- Appending to files
- Context managers (`with` statement)
- File paths and directories

**DevOps Use Cases:**
- Reading log files
- Writing configuration files
- Appending to audit logs
- Processing server outputs

**Key Code:**
```python
# Read log file
with open("server.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())

# Write config
with open("config.txt", "w") as file:
    file.write("server=192.168.1.10\n")
    file.write("port=8080\n")
```

---

### Day 13-14: Error Handling

**Topics:**
- try-except blocks
- Specific exception types
- finally clause
- Raising exceptions
- Custom exceptions

**DevOps Use Cases:**
- Handling missing files
- Network connection errors
- Invalid configuration
- Graceful degradation

**Key Code:**
```python
try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Config not found, using defaults")
    config = {"host": "localhost"}
except json.JSONDecodeError:
    print("Invalid JSON format")
finally:
    print("Config loading complete")
```

---

### Day 15-16: JSON Operations

**Topics:**
- JSON format basics
- `json.load()` and `json.dump()`
- `json.loads()` and `json.dumps()`
- Working with nested JSON
- Pretty printing JSON

**DevOps Use Cases:**
- API responses
- Configuration files
- Docker configs
- Kubernetes manifests
- Terraform state files

**Key Code:**
```python
import json

# Read JSON config
with open("servers.json", "r") as file:
    servers = json.load(file)

# Write JSON config
config = {
    "servers": [
        {"name": "web-1", "ip": "192.168.1.10"},
        {"name": "db-1", "ip": "192.168.1.20"}
    ]
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=2)
```

---

### Day 17-18: Date and Time

**Topics:**
- `datetime` module
- Current time (`datetime.now()`)
- Formatting dates (`strftime()`)
- Parsing dates (`strptime()`)
- Time arithmetic (`timedelta`)
- Timestamps

**DevOps Use Cases:**
- Log timestamps
- Backup scheduling
- Uptime calculation
- Performance metrics
- Retention policies

**Key Code:**
```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# Calculate uptime
start_time = datetime(2024, 12, 1, 10, 0, 0)
uptime = now - start_time
print(f"Uptime: {uptime.days} days")

# Schedule next backup
next_backup = now + timedelta(hours=24)
```

---

### Day 19-20: Command-Line Arguments

**Topics:**
- `sys.argv` basics
- `argparse` module
- Required vs optional arguments
- Argument types
- Help messages
- Flags and switches

**DevOps Use Cases:**
- Flexible deployment scripts
- Configurable monitoring tools
- Multi-environment support
- Debug modes
- Batch operations

**Key Code:**
```python
import argparse

parser = argparse.ArgumentParser(description='Server Health Check')
parser.add_argument('server', help='Server name')
parser.add_argument('--port', type=int, default=22, help='Port number')
parser.add_argument('--verbose', action='store_true', help='Verbose output')
parser.add_argument('--timeout', type=int, default=30, help='Timeout in seconds')

args = parser.parse_args()

print(f"Checking {args.server}:{args.port}")
if args.verbose:
    print(f"Timeout: {args.timeout}s")
```

---

## Week Project: Log Analyzer Tool

Build a comprehensive log analyzer that:
- Reads log files
- Parses timestamps and log levels
- Filters by severity (ERROR, WARNING, INFO)
- Generates statistics
- Exports reports
- Accepts command-line arguments

**Features:**
- Parse various log formats
- Count errors/warnings
- Find patterns
- Time-based filtering
- Export to JSON/CSV

---

## Practice Exercises

### Exercise 1: Config File Manager
Create a script that:
- Reads server config from JSON
- Validates required fields
- Updates configuration
- Saves changes back to file
- Handles errors gracefully

### Exercise 2: Log Rotation Script
Build a tool that:
- Checks log file size
- Rotates logs when size exceeds limit
- Adds timestamps to rotated files
- Keeps only N recent logs
- Compresses old logs

### Exercise 3: Backup Scheduler
Develop a script that:
- Calculates next backup time
- Creates timestamped backups
- Checks backup age
- Alerts if backup is overdue
- Maintains backup history

---

## Real-World DevOps Scenarios

### Scenario 1: Parse Nginx Access Logs
```python
import re
from datetime import datetime

def parse_nginx_log(line):
    # Parse: 192.168.1.1 - - [24/Dec/2024:10:30:45 +0000] "GET /api HTTP/1.1" 200 1234
    pattern = r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
    match = re.match(pattern, line)
    
    if match:
        return {
            "ip": match.group(1),
            "timestamp": match.group(2),
            "request": match.group(3),
            "status": int(match.group(4)),
            "size": int(match.group(5))
        }
    return None
```

### Scenario 2: Configuration Validator
```python
def validate_server_config(config):
    required_fields = ["name", "ip", "port"]
    
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    if not (1 <= config["port"] <= 65535):
        raise ValueError("Port must be between 1 and 65535")
    
    return True
```

### Scenario 3: Uptime Monitor
```python
from datetime import datetime, timedelta

class UptimeMonitor:
    def __init__(self, start_time):
        self.start_time = start_time
    
    def get_uptime(self):
        now = datetime.now()
        uptime = now - self.start_time
        
        days = uptime.days
        hours = uptime.seconds // 3600
        minutes = (uptime.seconds % 3600) // 60
        
        return f"{days}d {hours}h {minutes}m"
    
    def get_uptime_percentage(self, total_days=30):
        uptime = datetime.now() - self.start_time
        uptime_percent = (uptime.days / total_days) * 100
        return min(uptime_percent, 100)
```

---

## Common Patterns

### Pattern 1: Safe File Reading
```python
def read_config_safe(filename, default=None):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Config file {filename} not found")
        return default or {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filename}")
        return default or {}
```

### Pattern 2: Log Entry Parser
```python
def parse_log_entry(line):
    try:
        parts = line.split(" - ")
        timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
        level = parts[1]
        message = parts[2].strip()
        
        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
    except (IndexError, ValueError) as e:
        print(f"Failed to parse line: {line}")
        return None
```

### Pattern 3: Retry with Backoff
```python
import time

def retry_with_backoff(func, max_attempts=3, base_delay=1):
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            
            delay = base_delay * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed. Retrying in {delay}s...")
            time.sleep(delay)
```

---

## Tools and Libraries

### Essential Libraries:
- `json` - JSON parsing
- `datetime` - Date/time operations
- `argparse` - Command-line arguments
- `os` - File system operations
- `pathlib` - Modern path handling
- `re` - Regular expressions

### Installation:
```bash
# Most are built-in, but for additional tools:
pip install python-dateutil  # Advanced date parsing
pip install click            # Alternative to argparse
```

---

## Tips for Success

1. **Always use context managers** (`with` statement) for files
2. **Handle errors explicitly** - don't let scripts crash
3. **Validate input** before processing
4. **Use meaningful variable names** in parsers
5. **Test with edge cases** (empty files, malformed data)
6. **Add logging** to track script execution
7. **Document your code** with comments and docstrings

---

## Next Steps

After completing Week 3-4, you'll be ready for:
- Week 5-6: DevOps-specific Python (APIs, system commands)
- Week 7-8: Real-world projects
- Building your own automation tools
- Contributing to open-source DevOps projects

---

**Keep practicing! Build tools that solve real problems you face! 🚀**
