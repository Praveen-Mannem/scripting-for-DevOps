# Python for DevOps - Complete Learning Plan

## 📚 8-Week Detailed Curriculum

---

## Week 1-2: Python Basics (Foundation)

### Day 1: Getting Started
**Goal:** Install Python and write your first script

#### What You'll Learn:
- Installing Python
- Running Python scripts
- Print statements
- Comments

#### Hands-on Exercise:
```python
# My first Python script
print("Hello, DevOps World!")
print("My name is Praveen")
print("I'm learning Python for DevOps")
```

**Task:** Create a file called `hello.py` and run it

---

### Day 2: Variables and Data Types
**Goal:** Store and use information

#### What You'll Learn:
```python
# Variables - storing information
name = "Praveen"
age = 25
is_learning = True
salary = 50000.50

# Using variables
print("Name:", name)
print("Age:", age)
print("Learning DevOps:", is_learning)
```

#### Practice Exercise:
Create a script that stores:
- Your name
- Your city
- Number of years you want to work in DevOps
- Print them in a nice format

---

### Day 3: User Input and String Operations
**Goal:** Make interactive scripts

#### What You'll Learn:
```python
# Getting input from user
name = input("What's your name? ")
city = input("Which city are you from? ")

# String operations
message = "Hello " + name + " from " + city
print(message)

# Better way (f-strings)
print(f"Hello {name} from {city}!")
```

#### Practice Exercise:
Create a script that asks:
- Server name
- IP address
- Status (running/stopped)
- Print a status report

---

### Day 4: Numbers and Math Operations
**Goal:** Work with numbers (important for monitoring, calculations)

#### What You'll Learn:
```python
# Math operations
cpu_usage = 75
memory_usage = 60
disk_usage = 45

# Calculate average
total = cpu_usage + memory_usage + disk_usage
average = total / 3

print(f"Average resource usage: {average}%")

# Check if critical
if average > 70:
    print("⚠️ WARNING: High resource usage!")
else:
    print("✅ System running normally")
```

#### Practice Exercise:
Create a disk space calculator that:
- Takes total disk space
- Takes used space
- Calculates free space and percentage used

---

### Day 5: Lists (Collections of Data)
**Goal:** Store multiple items

#### What You'll Learn:
```python
# Lists - storing multiple servers
servers = ["web-server-1", "db-server-1", "app-server-1"]

# Accessing items
print(servers[0])  # First server
print(servers[-1])  # Last server

# Adding servers
servers.append("cache-server-1")

# Loop through servers
for server in servers:
    print(f"Checking {server}...")
```

#### Practice Exercise:
Create a script that:
- Stores a list of 5 server names
- Prints each server with a number
- Adds a new server
- Prints the updated list

---

### Day 6: Dictionaries (Key-Value Pairs)
**Goal:** Store structured data (like JSON)

#### What You'll Learn:
```python
# Dictionary - server information
server = {
    "name": "web-server-1",
    "ip": "192.168.1.10",
    "status": "running",
    "cpu": 45,
    "memory": 60
}

# Accessing data
print(f"Server: {server['name']}")
print(f"IP: {server['ip']}")
print(f"CPU Usage: {server['cpu']}%")

# Multiple servers
servers = [
    {"name": "web-1", "ip": "192.168.1.10", "status": "running"},
    {"name": "db-1", "ip": "192.168.1.20", "status": "stopped"},
    {"name": "app-1", "ip": "192.168.1.30", "status": "running"}
]

for server in servers:
    print(f"{server['name']} ({server['ip']}) - {server['status']}")
```

#### Practice Exercise:
Create a server inventory with 3 servers, each having:
- Name, IP, OS, Status
- Print a formatted report

---

### Day 7: If-Else Conditions
**Goal:** Make decisions in scripts

#### What You'll Learn:
```python
# Checking server status
cpu_usage = 85

if cpu_usage > 90:
    print("🔴 CRITICAL: CPU usage very high!")
elif cpu_usage > 70:
    print("🟡 WARNING: CPU usage high")
else:
    print("🟢 OK: CPU usage normal")

# Multiple conditions
memory = 75
cpu = 85

if cpu > 80 and memory > 80:
    print("Both CPU and Memory are high!")
elif cpu > 80 or memory > 80:
    print("Either CPU or Memory is high")
else:
    print("System is healthy")
```

#### Practice Exercise:
Create a health check script that:
- Checks CPU, Memory, Disk
- Prints different alerts based on thresholds
- Gives overall system status

---

### Day 8: Loops (Automation!)
**Goal:** Repeat tasks automatically

#### What You'll Learn:
```python
# For loop - check multiple servers
servers = ["web-1", "web-2", "web-3", "db-1", "db-2"]

for server in servers:
    print(f"Pinging {server}...")
    print(f"{server} is responding ✓")
    print("---")

# While loop - keep checking until condition
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}: Trying to connect...")
    if attempts == 3:
        print("Connected successfully!")
        break
```

#### Practice Exercise:
Create a script that:
- Loops through 10 servers
- Simulates a health check for each
- Counts how many are "healthy"

---

### Day 9-10: Functions (Reusable Code)
**Goal:** Write organized, reusable code

#### What You'll Learn:
```python
# Function to check server health
def check_server_health(server_name, cpu, memory):
    print(f"\n=== Checking {server_name} ===")
    
    if cpu > 80 or memory > 80:
        return "UNHEALTHY"
    else:
        return "HEALTHY"

# Using the function
status1 = check_server_health("web-1", 45, 60)
print(f"Status: {status1}")

status2 = check_server_health("db-1", 85, 90)
print(f"Status: {status2}")

# Function with default values
def ping_server(server_name, timeout=5):
    print(f"Pinging {server_name} with {timeout}s timeout...")
    return True

ping_server("web-1")
ping_server("db-1", timeout=10)
```

#### Practice Exercise:
Create functions for:
- `calculate_disk_usage(total, used)` - returns percentage
- `check_service_status(service_name)` - returns running/stopped
- `restart_service(service_name)` - prints restart message

---

### Week 1-2 Project: Server Monitoring Dashboard

Create a complete script that monitors multiple servers and displays their health status.

**File:** `week-1-2-basics/project-server-monitor/server_monitor.py`

```python
# server_monitor.py

def check_health(name, cpu, memory, disk):
    """Check if server is healthy"""
    if cpu > 80 or memory > 80 or disk > 80:
        return "🔴 CRITICAL"
    elif cpu > 60 or memory > 60 or disk > 60:
        return "🟡 WARNING"
    else:
        return "🟢 HEALTHY"

# Server data
servers = [
    {"name": "web-1", "cpu": 45, "memory": 55, "disk": 40},
    {"name": "web-2", "cpu": 85, "memory": 70, "disk": 60},
    {"name": "db-1", "cpu": 60, "memory": 90, "disk": 75},
    {"name": "app-1", "cpu": 30, "memory": 40, "disk": 35}
]

# Monitor all servers
print("=" * 50)
print("SERVER MONITORING DASHBOARD")
print("=" * 50)

healthy_count = 0
warning_count = 0
critical_count = 0

for server in servers:
    status = check_health(
        server["name"],
        server["cpu"],
        server["memory"],
        server["disk"]
    )
    
    print(f"\n{server['name']}")
    print(f"  CPU: {server['cpu']}% | Memory: {server['memory']}% | Disk: {server['disk']}%")
    print(f"  Status: {status}")
    
    if "HEALTHY" in status:
        healthy_count += 1
    elif "WARNING" in status:
        warning_count += 1
    else:
        critical_count += 1

print("\n" + "=" * 50)
print(f"Summary: {healthy_count} Healthy | {warning_count} Warning | {critical_count} Critical")
print("=" * 50)
```

---

## Week 3-4: Intermediate Python for DevOps

### Day 11-12: Working with Files
**Goal:** Read and write files (logs, configs)

#### What You'll Learn:
```python
# Writing to a file
with open("server_log.txt", "w") as file:
    file.write("Server started at 10:00 AM\n")
    file.write("All services running\n")
    file.write("CPU: 45%, Memory: 60%\n")

# Reading from a file
with open("server_log.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("server_log.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open("server_log.txt", "a") as file:
    file.write("New entry: Backup completed\n")
```

#### Practice Exercise:
Create a script that:
- Writes server status to a log file
- Reads and displays the log
- Adds timestamp to each entry

---

### Day 13-14: Error Handling
**Goal:** Handle errors gracefully

#### What You'll Learn:
```python
# Try-except for error handling
def connect_to_server(ip):
    try:
        print(f"Connecting to {ip}...")
        # Simulate connection
        if ip == "":
            raise ValueError("IP address cannot be empty")
        print("Connected successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Connection attempt completed")

connect_to_server("192.168.1.10")
connect_to_server("")

# File handling with error checking
try:
    with open("config.txt", "r") as file:
        config = file.read()
except FileNotFoundError:
    print("Config file not found! Creating default...")
    with open("config.txt", "w") as file:
        file.write("default_config=true\n")
```

#### Practice Exercise:
Create a script that:
- Tries to read a server list file
- If file doesn't exist, creates it with default servers
- Handles invalid data gracefully

---

### Day 15-16: Working with JSON
**Goal:** Parse configuration files (JSON is everywhere in DevOps)

#### What You'll Learn:
```python
import json

# Python dictionary to JSON
server_config = {
    "servers": [
        {"name": "web-1", "ip": "192.168.1.10", "port": 80},
        {"name": "db-1", "ip": "192.168.1.20", "port": 5432}
    ],
    "environment": "production"
}

# Write to JSON file
with open("config.json", "w") as file:
    json.dump(server_config, file, indent=2)

# Read from JSON file
with open("config.json", "r") as file:
    config = json.load(file)
    
print(f"Environment: {config['environment']}")
for server in config['servers']:
    print(f"{server['name']}: {server['ip']}:{server['port']}")
```

#### Practice Exercise:
Create a configuration management script that:
- Reads server config from JSON
- Allows adding new servers
- Saves updated config back to JSON

---

### Day 17-18: Working with Dates and Times
**Goal:** Timestamps, scheduling, log analysis

#### What You'll Learn:
```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
print(f"Current time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate uptime
start_time = datetime(2024, 12, 1, 10, 0, 0)
uptime = now - start_time
print(f"Server uptime: {uptime.days} days")

# Future time
backup_time = now + timedelta(hours=24)
print(f"Next backup: {backup_time}")

# Parse log timestamps
log_entry = "2024-12-24 10:30:45 - Server started"
timestamp = datetime.strptime("2024-12-24 10:30:45", "%Y-%m-%d %H:%M:%S")
```

#### Practice Exercise:
Create a log analyzer that:
- Reads log file with timestamps
- Calculates time between events
- Finds entries from last 24 hours

---

### Day 19-20: Command Line Arguments
**Goal:** Make scripts flexible with arguments

#### What You'll Learn:
```python
import sys

# Basic arguments
# Run: python script.py web-1 192.168.1.10
if len(sys.argv) > 1:
    server_name = sys.argv[1]
    server_ip = sys.argv[2]
    print(f"Checking {server_name} at {server_ip}")
else:
    print("Usage: python script.py <server_name> <server_ip>")

# Better way with argparse
import argparse

parser = argparse.ArgumentParser(description='Server Health Check')
parser.add_argument('server', help='Server name')
parser.add_argument('--cpu', type=int, default=80, help='CPU threshold')
parser.add_argument('--memory', type=int, default=80, help='Memory threshold')

args = parser.parse_args()
print(f"Checking {args.server}")
print(f"CPU threshold: {args.cpu}%")
print(f"Memory threshold: {args.memory}%")
```

#### Practice Exercise:
Create a flexible monitoring script that accepts:
- Server name (required)
- Check type (cpu/memory/disk)
- Threshold value (optional)

---

### Week 3-4 Project: Log Analyzer Tool

**File:** `week-3-4-intermediate/project-log-analyzer/log_analyzer.py`

```python
# log_analyzer.py
import json
from datetime import datetime
import argparse

def parse_log_line(line):
    """Parse a log line and extract information"""
    try:
        parts = line.split(" - ")
        timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
        level = parts[1]
        message = parts[2].strip()
        return {"timestamp": timestamp, "level": level, "message": message}
    except:
        return None

def analyze_logs(filename, level_filter=None):
    """Analyze log file and generate report"""
    logs = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    if level_filter is None or log["level"] == level_filter:
                        logs.append(log)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return
    
    # Generate statistics
    total = len(logs)
    errors = sum(1 for log in logs if log["level"] == "ERROR")
    warnings = sum(1 for log in logs if log["level"] == "WARNING")
    
    print(f"\n=== Log Analysis Report ===")
    print(f"Total entries: {total}")
    print(f"Errors: {errors}")
    print(f"Warnings: {warnings}")
    
    if errors > 0:
        print(f"\nRecent errors:")
        for log in logs[-5:]:
            if log["level"] == "ERROR":
                print(f"  {log['timestamp']}: {log['message']}")

# Command line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze server logs')
    parser.add_argument('logfile', help='Path to log file')
    parser.add_argument('--level', choices=['ERROR', 'WARNING', 'INFO'], 
                       help='Filter by log level')
    
    args = parser.parse_args()
    analyze_logs(args.logfile, args.level)
```

---

## Week 5-6: DevOps-Specific Python

### Day 21-23: Running System Commands

```python
import subprocess

# Run a command
result = subprocess.run(['ping', '-n', '4', 'google.com'], 
                       capture_output=True, text=True)
print(result.stdout)

# Check if command succeeded
if result.returncode == 0:
    print("Command successful!")
else:
    print("Command failed!")

# DevOps example: Check disk space
def check_disk_space():
    result = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'],
                           capture_output=True, text=True)
    print(result.stdout)

check_disk_space()
```

---

### Day 24-26: Working with APIs

```python
import requests
import json

# GET request example
def get_server_status(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

# POST request example
def create_server(api_url, server_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=server_data, headers=headers)
    return response.json()

# Example: GitHub API
def get_repo_info(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Repo: {data['name']}")
        print(f"Stars: {data['stargazers_count']}")
        print(f"Forks: {data['forks_count']}")

get_repo_info("kubernetes", "kubernetes")
```

---

### Day 27-28: Environment Variables & Configuration

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
api_key = os.getenv('API_KEY', 'default_key')
environment = os.getenv('ENVIRONMENT', 'development')
db_host = os.getenv('DB_HOST', 'localhost')

print(f"Environment: {environment}")
print(f"Database: {db_host}")

# Set environment variable
os.environ['NEW_VAR'] = 'value'

# DevOps example: Configuration management
class Config:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.db_host = os.getenv('DB_HOST')
        self.debug = os.getenv('DEBUG', 'False') == 'True'
    
    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY not set!")
        if not self.db_host:
            raise ValueError("DB_HOST not set!")

config = Config()
config.validate()
```

---

## Week 7-8: Real DevOps Projects

### Project 1: Automated Backup Script

**File:** `week-7-8-projects/backup-automation/backup.py`

```python
# backup_automation.py
import os
import shutil
from datetime import datetime
import zipfile

def create_backup(source_dir, backup_dir):
    """Create timestamped backup of directory"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_name)
    
    print(f"Creating backup: {backup_name}")
    
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    
    print(f"Backup created: {backup_path}")
    return backup_path

def cleanup_old_backups(backup_dir, keep_count=5):
    """Keep only the latest N backups"""
    backups = sorted([f for f in os.listdir(backup_dir) if f.startswith('backup_')])
    
    if len(backups) > keep_count:
        for old_backup in backups[:-keep_count]:
            os.remove(os.path.join(backup_dir, old_backup))
            print(f"Removed old backup: {old_backup}")

# Usage
if __name__ == "__main__":
    create_backup("C:\\MyProject", "C:\\Backups")
    cleanup_old_backups("C:\\Backups", keep_count=3)
```

---

### Project 2: Server Health Monitor with Alerts

**File:** `week-7-8-projects/health-monitor/monitor.py`

```python
# health_monitor.py
import psutil
from datetime import datetime

class ServerMonitor:
    def __init__(self, cpu_threshold=80, memory_threshold=80, disk_threshold=80):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.disk_threshold = disk_threshold
        self.alerts = []
    
    def check_cpu(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > self.cpu_threshold:
            self.alerts.append(f"🔴 CPU usage high: {cpu_percent}%")
        return cpu_percent
    
    def check_memory(self):
        memory = psutil.virtual_memory()
        if memory.percent > self.memory_threshold:
            self.alerts.append(f"🔴 Memory usage high: {memory.percent}%")
        return memory.percent
    
    def check_disk(self):
        disk = psutil.disk_usage('/')
        if disk.percent > self.disk_threshold:
            self.alerts.append(f"🔴 Disk usage high: {disk.percent}%")
        return disk.percent
    
    def generate_report(self):
        cpu = self.check_cpu()
        memory = self.check_memory()
        disk = self.check_disk()
        
        report = f"""
        === Server Health Report ===
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        CPU Usage: {cpu}%
        Memory Usage: {memory}%
        Disk Usage: {disk}%
        
        """
        
        if self.alerts:
            report += "\n⚠️ ALERTS:\n"
            for alert in self.alerts:
                report += f"  {alert}\n"
        else:
            report += "✅ All systems normal\n"
        
        return report

# Usage
if __name__ == "__main__":
    monitor = ServerMonitor(cpu_threshold=70, memory_threshold=75)
    report = monitor.generate_report()
    print(report)
```

---

### Project 3: Deployment Automation Script

**File:** `week-7-8-projects/deployment-script/deploy.py`

```python
# deploy.py
import subprocess
import sys
from datetime import datetime

class Deployer:
    def __init__(self, app_name, environment):
        self.app_name = app_name
        self.environment = environment
        self.log_file = f"deploy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    def log(self, message):
        """Log deployment steps"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(self.log_file, 'a') as f:
            f.write(log_message + '\n')
    
    def run_command(self, command, description):
        """Run a command and log output"""
        self.log(f"Running: {description}")
        try:
            result = subprocess.run(command, shell=True, 
                                   capture_output=True, text=True, check=True)
            self.log(f"✅ Success: {description}")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"❌ Failed: {description}")
            self.log(f"Error: {e.stderr}")
            return False
    
    def deploy(self):
        """Main deployment workflow"""
        self.log(f"Starting deployment of {self.app_name} to {self.environment}")
        
        steps = [
            ("git pull origin main", "Pulling latest code"),
            ("npm install", "Installing dependencies"),
            ("npm run build", "Building application"),
            ("npm test", "Running tests"),
        ]
        
        for command, description in steps:
            if not self.run_command(command, description):
                self.log("❌ Deployment failed!")
                return False
        
        self.log("✅ Deployment completed successfully!")
        return True
    
    def rollback(self):
        """Rollback to previous version"""
        self.log("🔄 Rolling back to previous version")
        self.run_command("git reset --hard HEAD~1", "Reverting code")
        self.run_command("npm install", "Reinstalling dependencies")
        self.log("✅ Rollback completed")

# Usage
if __name__ == "__main__":
    deployer = Deployer("MyApp", "production")
    
    if deployer.deploy():
        print("\n🎉 Deployment successful!")
    else:
        print("\n❌ Deployment failed. Rolling back...")
        deployer.rollback()
```

---

## 🎯 Next Steps After Completing This Course

### 1. Learn DevOps Tools with Python:
- **Docker**: `docker-py` library
- **Kubernetes**: `kubernetes` Python client
- **AWS**: `boto3` library
- **Ansible**: Python-based automation
- **Terraform**: Python wrappers

### 2. Advanced Topics:
- Asynchronous programming (`asyncio`)
- Multi-threading for parallel tasks
- Database operations (PostgreSQL, MongoDB)
- Message queues (RabbitMQ, Kafka)

### 3. Build Real Projects:
- CI/CD pipeline automation
- Infrastructure monitoring dashboard
- Log aggregation system
- Auto-scaling script
- Backup and disaster recovery automation

---

## 📚 Resources

### Documentation:
- Official Python Docs: docs.python.org
- Real Python: realpython.com
- Python for DevOps Book

### Practice:
- HackerRank Python challenges
- LeetCode easy problems
- Automate the Boring Stuff with Python

### Communities:
- r/learnpython
- Python Discord servers
- Stack Overflow

---

**Remember:** 
- Practice every day, even if just 30 minutes
- Don't just copy code - understand it
- Break things and fix them - that's how you learn!
- Ask questions when stuck
- Build your own variations of projects

**You've got this! 🚀**
