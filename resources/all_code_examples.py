# Complete Python DevOps Code Examples
# All 8 weeks of code in one reference file

"""
This file contains all code examples from the 8-week course.
Use this as a quick reference while learning.
Each section corresponds to a day/week in the course.
"""

# ============================================================================
# WEEK 1-2: PYTHON BASICS
# ============================================================================

# --- DAY 1: HELLO WORLD ---
print("Hello, DevOps World!")

# Comments
# This is a single line comment

"""
This is a multi-line comment
or docstring
"""

# --- DAY 2: VARIABLES AND DATA TYPES ---

# Strings
server_name = "web-server-1"
ip_address = "192.168.1.10"

# Integers
cpu_usage = 75
port = 8080

# Floats
memory_gb = 15.5
response_time = 0.125

# Booleans
is_running = True
has_backup = False

# Type checking
print(type(server_name))  # <class 'str'>

# String formatting
message = f"Server {server_name} at {ip_address}"
print(message)

# --- DAY 3: USER INPUT AND STRINGS ---

# Getting input
name = input("Enter server name: ")
port = input("Enter port: ")

# String methods
text = "  Hello World  "
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.strip())      # Hello World
print(text.replace("World", "Python"))  # Hello Python

# String splitting
log = "2024-12-24 ERROR Database connection failed"
parts = log.split(" ")
print(parts)  # ['2024-12-24', 'ERROR', 'Database', 'connection', 'failed']

# --- DAY 4: NUMBERS AND MATH ---

# Basic math
cpu = 75
memory = 60
total = cpu + memory      # Addition
diff = cpu - memory       # Subtraction
product = cpu * 2         # Multiplication
quotient = cpu / 2        # Division
floor_div = cpu // 2      # Floor division
remainder = cpu % 10      # Modulus
power = cpu ** 2          # Exponentiation

# Comparison operators
print(cpu > 50)           # True
print(cpu == 75)          # True
print(cpu != 60)          # True
print(cpu >= 75)          # True

# --- DAY 5: LISTS ---

# Creating lists
servers = ["web-1", "web-2", "db-1", "app-1"]
ports = [80, 443, 3306, 8080]

# Accessing items
first_server = servers[0]      # web-1
last_server = servers[-1]      # app-1

# List methods
servers.append("cache-1")      # Add to end
servers.insert(0, "lb-1")      # Insert at position
servers.remove("db-1")         # Remove by value
popped = servers.pop()         # Remove and return last
length = len(servers)          # Get length

# List slicing
first_two = servers[0:2]       # First 2 items
last_two = servers[-2:]        # Last 2 items

# Looping through lists
for server in servers:
    print(f"Checking {server}")

# List comprehension
squared = [x**2 for x in range(10)]
active_servers = [s for s in servers if "web" in s]

# --- DAY 6: DICTIONARIES ---

# Creating dictionaries
server = {
    "name": "web-server-1",
    "ip": "192.168.1.10",
    "port": 80,
    "status": "running",
    "cpu": 45,
    "memory": 60
}

# Accessing values
name = server["name"]
cpu = server.get("cpu", 0)  # With default value

# Modifying dictionaries
server["cpu"] = 75           # Update value
server["disk"] = 40          # Add new key
del server["port"]           # Delete key

# Dictionary methods
keys = server.keys()         # All keys
values = server.values()     # All values
items = server.items()       # Key-value pairs

# Looping through dictionaries
for key, value in server.items():
    print(f"{key}: {value}")

# List of dictionaries (common in DevOps)
servers = [
    {"name": "web-1", "ip": "192.168.1.10", "cpu": 45},
    {"name": "db-1", "ip": "192.168.1.20", "cpu": 75},
    {"name": "app-1", "ip": "192.168.1.30", "cpu": 60}
]

for server in servers:
    print(f"{server['name']}: CPU {server['cpu']}%")

# --- DAY 7: CONDITIONS ---

# If-elif-else
cpu = 85

if cpu > 90:
    status = "CRITICAL"
elif cpu > 70:
    status = "WARNING"
else:
    status = "OK"

# Logical operators
cpu = 85
memory = 75

if cpu > 80 and memory > 80:
    print("Both high")
elif cpu > 80 or memory > 80:
    print("One is high")
else:
    print("Both normal")

# Not operator
is_healthy = False
if not is_healthy:
    print("Server needs attention")

# Ternary operator
status = "Active" if is_running else "Inactive"

# --- DAY 8: LOOPS ---

# For loop with range
for i in range(5):
    print(f"Iteration {i}")

# For loop with list
servers = ["web-1", "web-2", "db-1"]
for server in servers:
    print(f"Checking {server}")

# Enumerate (get index and value)
for index, server in enumerate(servers):
    print(f"{index}: {server}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)

# Nested loops
for server in ["web-1", "web-2"]:
    for port in [80, 443]:
        print(f"{server}:{port}")

# --- DAY 9-10: FUNCTIONS ---

# Basic function
def greet(name):
    return f"Hello, {name}!"

result = greet("Praveen")

# Function with default parameters
def connect(host, port=22, timeout=30):
    return f"Connecting to {host}:{port} (timeout: {timeout}s)"

# Multiple return values
def get_stats():
    cpu = 75
    memory = 60
    disk = 45
    return cpu, memory, disk

c, m, d = get_stats()

# Function with type hints (optional but good practice)
def check_health(cpu: int, memory: int) -> str:
    if cpu > 80 or memory > 80:
        return "UNHEALTHY"
    return "HEALTHY"

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
add = lambda x, y: x + y

# ============================================================================
# WEEK 3-4: INTERMEDIATE PYTHON
# ============================================================================

# --- FILE OPERATIONS ---

# Writing to file
with open("server_log.txt", "w") as file:
    file.write("Server started\n")
    file.write("All services running\n")

# Reading from file
with open("server_log.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("server_log.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to file
with open("server_log.txt", "a") as file:
    file.write("New log entry\n")

# Reading all lines into list
with open("server_log.txt", "r") as file:
    lines = file.readlines()

# --- ERROR HANDLING ---

# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    with open("config.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Unexpected error: {e}")

# Finally clause
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always executes

# Raising exceptions
def check_port(port):
    if port < 1 or port > 65535:
        raise ValueError("Port must be between 1 and 65535")
    return port

# --- JSON OPERATIONS ---

import json

# Python dict to JSON
server_config = {
    "servers": [
        {"name": "web-1", "ip": "192.168.1.10"},
        {"name": "db-1", "ip": "192.168.1.20"}
    ],
    "environment": "production"
}

# Write JSON to file
with open("config.json", "w") as file:
    json.dump(server_config, file, indent=2)

# Read JSON from file
with open("config.json", "r") as file:
    config = json.load(file)

# JSON string to Python
json_string = '{"name": "web-1", "cpu": 75}'
data = json.loads(json_string)

# Python to JSON string
json_output = json.dumps(server_config, indent=2)

# --- DATE AND TIME ---

from datetime import datetime, timedelta

# Current time
now = datetime.now()
print(now)

# Formatted time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-12-24 21:00:00

# Parse string to datetime
dt = datetime.strptime("2024-12-24 10:30:00", "%Y-%m-%d %H:%M:%S")

# Time arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

# Time difference
start = datetime(2024, 12, 1, 10, 0, 0)
end = datetime.now()
uptime = end - start
print(f"Uptime: {uptime.days} days")

# --- COMMAND LINE ARGUMENTS ---

import sys

# Basic arguments
# Run: python script.py arg1 arg2
if len(sys.argv) > 1:
    script_name = sys.argv[0]
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]

# Better way with argparse
import argparse

parser = argparse.ArgumentParser(description='Server Monitor')
parser.add_argument('server', help='Server name')
parser.add_argument('--port', type=int, default=22, help='Port number')
parser.add_argument('--verbose', action='store_true', help='Verbose output')

args = parser.parse_args()
print(f"Server: {args.server}")
print(f"Port: {args.port}")
print(f"Verbose: {args.verbose}")

# ============================================================================
# WEEK 5-6: DEVOPS-SPECIFIC PYTHON
# ============================================================================

# --- RUNNING SYSTEM COMMANDS ---

import subprocess

# Run command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)  # 0 = success

# Run with shell
result = subprocess.run('echo "Hello"', shell=True, capture_output=True, text=True)

# Check if command succeeded
try:
    subprocess.run(['ls', '/nonexistent'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")

# --- WORKING WITH APIs ---

import requests

# GET request
response = requests.get('https://api.github.com/repos/python/cpython')
if response.status_code == 200:
    data = response.json()
    print(data['name'])
    print(data['stargazers_count'])

# POST request
data = {"key": "value"}
response = requests.post(
    'https://api.example.com/create',
    json=data,
    headers={'Authorization': 'Bearer token123'}
)

# Error handling with requests
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raise exception for bad status codes
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# --- ENVIRONMENT VARIABLES ---

import os

# Read environment variable
api_key = os.getenv('API_KEY', 'default_value')
db_host = os.environ.get('DB_HOST', 'localhost')

# Set environment variable
os.environ['MY_VAR'] = 'value'

# Check if variable exists
if 'API_KEY' in os.environ:
    print("API_KEY is set")

# Using python-dotenv
from dotenv import load_dotenv

load_dotenv()  # Load from .env file
api_key = os.getenv('API_KEY')

# ============================================================================
# WEEK 7-8: REAL DEVOPS PROJECTS
# ============================================================================

# --- PROJECT 1: BACKUP AUTOMATION ---

import os
import shutil
from datetime import datetime
import zipfile

def create_backup(source_dir, backup_dir):
    """Create timestamped backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_name)
    
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    
    return backup_path

def cleanup_old_backups(backup_dir, keep_count=5):
    """Keep only latest N backups"""
    backups = sorted([f for f in os.listdir(backup_dir) if f.startswith('backup_')])
    
    if len(backups) > keep_count:
        for old_backup in backups[:-keep_count]:
            os.remove(os.path.join(backup_dir, old_backup))

# --- PROJECT 2: SERVER HEALTH MONITOR ---

import psutil
from datetime import datetime

class ServerMonitor:
    def __init__(self, cpu_threshold=80, memory_threshold=80):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.alerts = []
    
    def check_cpu(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > self.cpu_threshold:
            self.alerts.append(f"CPU high: {cpu_percent}%")
        return cpu_percent
    
    def check_memory(self):
        memory = psutil.virtual_memory()
        if memory.percent > self.memory_threshold:
            self.alerts.append(f"Memory high: {memory.percent}%")
        return memory.percent
    
    def check_disk(self):
        disk = psutil.disk_usage('/')
        return disk.percent
    
    def generate_report(self):
        cpu = self.check_cpu()
        memory = self.check_memory()
        disk = self.check_disk()
        
        report = f"""
=== Server Health Report ===
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
CPU: {cpu}%
Memory: {memory}%
Disk: {disk}%
"""
        if self.alerts:
            report += "\nAlerts:\n" + "\n".join(self.alerts)
        
        return report

# --- PROJECT 3: DEPLOYMENT AUTOMATION ---

import subprocess
from datetime import datetime

class Deployer:
    def __init__(self, app_name, environment):
        self.app_name = app_name
        self.environment = environment
        self.log_file = f"deploy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    def log(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(self.log_file, 'a') as f:
            f.write(log_message + '\n')
    
    def run_command(self, command, description):
        self.log(f"Running: {description}")
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            self.log(f"Success: {description}")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"Failed: {description}")
            self.log(f"Error: {e.stderr}")
            return False
    
    def deploy(self):
        self.log(f"Starting deployment of {self.app_name} to {self.environment}")
        
        steps = [
            ("git pull origin main", "Pulling latest code"),
            ("npm install", "Installing dependencies"),
            ("npm run build", "Building application"),
            ("npm test", "Running tests"),
        ]
        
        for command, description in steps:
            if not self.run_command(command, description):
                self.log("Deployment failed!")
                return False
        
        self.log("Deployment completed successfully!")
        return True

# ============================================================================
# COMMON DEVOPS PATTERNS
# ============================================================================

# Retry logic
import time

def retry(func, max_attempts=3, delay=1):
    """Retry a function with exponential backoff"""
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            wait_time = delay * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed. Retrying in {wait_time}s...")
            time.sleep(wait_time)

# Configuration management
class Config:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.db_host = os.getenv('DB_HOST', 'localhost')
        self.debug = os.getenv('DEBUG', 'False') == 'True'
    
    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY not set")
        return True

# Logging setup
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
logger.warning("This is a warning")
logger.error("This is an error")

# ============================================================================
# END OF CODE EXAMPLES
# ============================================================================

"""
This file contains the core concepts from all 8 weeks.
Use it as a reference while working through the course.

Remember:
- Practice by typing code yourself
- Experiment with variations
- Build your own projects
- Keep learning!
"""
