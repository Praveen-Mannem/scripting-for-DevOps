# Day 2: Variables and Data Types

Welcome to Day 2! Today you'll learn how to store and work with different types of data in Python.

## Learning Objectives

By the end of today, you will:
- ✅ Understand what variables are
- ✅ Know the main data types in Python
- ✅ Store and use different types of information
- ✅ Print variables in formatted ways

---

## What are Variables?

Variables are like **labeled boxes** that store information. You can put data in them and use them later.

```python
# Think of it like this:
server_name = "web-server-1"  # A box labeled "server_name" containing "web-server-1"
```

---

## Variable Rules

### ✅ Good Variable Names:
```python
server_name = "web-1"
cpu_usage = 75
is_running = True
total_memory_gb = 16
```

### ❌ Bad Variable Names:
```python
1server = "web-1"      # Can't start with number
server-name = "web-1"  # Can't use hyphens
server name = "web-1"  # Can't have spaces
```

### Best Practices:
- Use lowercase with underscores: `server_name`
- Be descriptive: `cpu_usage` not `c`
- Use meaningful names: `total_servers` not `x`

---

## Data Types

### 1. Strings (Text)

```python
# Strings - text data
server_name = "web-server-1"
ip_address = "192.168.1.10"
status = "running"

# Can use single or double quotes
message1 = "Hello"
message2 = 'Hello'

# Print strings
print(server_name)
print("Server:", server_name)
```

### 2. Integers (Whole Numbers)

```python
# Integers - whole numbers
cpu_usage = 75
memory_usage = 60
disk_usage = 45
port = 8080
server_count = 10

# Math with integers
total = cpu_usage + memory_usage
print("Total usage:", total)
```

### 3. Floats (Decimal Numbers)

```python
# Floats - decimal numbers
cpu_percent = 75.5
memory_gb = 15.8
disk_tb = 2.5
response_time = 0.125

# Math with floats
average = (cpu_percent + memory_gb) / 2
print("Average:", average)
```

### 4. Booleans (True/False)

```python
# Booleans - True or False
is_running = True
is_healthy = False
has_backup = True
needs_restart = False

# Use in conditions (you'll learn more tomorrow)
if is_running:
    print("Server is running")
```

---

## Checking Data Types

```python
server_name = "web-1"
cpu_usage = 75
price = 99.99
is_active = True

# Check the type
print(type(server_name))  # <class 'str'>
print(type(cpu_usage))    # <class 'int'>
print(type(price))        # <class 'float'>
print(type(is_active))    # <class 'bool'>
```

---

## Working with Variables

### Storing Information

```python
# Server information
server_name = "web-server-1"
ip_address = "192.168.1.10"
cpu_usage = 45
memory_usage = 60
is_running = True

# Print all information
print("Server Name:", server_name)
print("IP Address:", ip_address)
print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory_usage, "%")
print("Running:", is_running)
```

### Changing Variables

```python
# Variables can change
cpu_usage = 45
print("CPU:", cpu_usage)  # 45

cpu_usage = 75
print("CPU:", cpu_usage)  # 75

cpu_usage = 90
print("CPU:", cpu_usage)  # 90
```

### Using Variables in Calculations

```python
# Calculate average resource usage
cpu = 75
memory = 60
disk = 45

total = cpu + memory + disk
average = total / 3

print("Average usage:", average, "%")
```

---

## String Formatting

### Method 1: Concatenation (Joining)

```python
server = "web-1"
status = "running"

message = "Server " + server + " is " + status
print(message)  # Server web-1 is running
```

### Method 2: f-strings (Recommended!)

```python
server = "web-1"
cpu = 75

# f-string - put 'f' before the quote
message = f"Server {server} has {cpu}% CPU usage"
print(message)

# Can do math inside f-strings
print(f"Double CPU: {cpu * 2}%")
```

### Method 3: format()

```python
server = "web-1"
cpu = 75

message = "Server {} has {}% CPU".format(server, cpu)
print(message)
```

---

## Practice Exercises

### Exercise 1: Personal Information

Create `exercise1.py`:

```python
# Exercise 1: Store your information
name = "Your Name"
city = "Your City"
age = 25
is_learning_python = True

# Print using f-strings
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Learning Python: {is_learning_python}")
```

---

### Exercise 2: Server Information

Create `exercise2.py`:

```python
# Exercise 2: Server details
server_name = "web-server-1"
ip_address = "192.168.1.10"
port = 8080
cpu_usage = 45.5
memory_usage = 60.2
is_active = True

# Print a formatted report
print("=" * 40)
print("SERVER STATUS REPORT")
print("=" * 40)
print(f"Server: {server_name}")
print(f"IP: {ip_address}:{port}")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Status: {'Active' if is_active else 'Inactive'}")
print("=" * 40)
```

---

### Exercise 3: Resource Calculator

Create `exercise3.py`:

```python
# Exercise 3: Calculate resource usage
cpu = 75
memory = 60
disk = 45

# Calculate total and average
total = cpu + memory + disk
average = total / 3

# Print results
print(f"CPU: {cpu}%")
print(f"Memory: {memory}%")
print(f"Disk: {disk}%")
print(f"Total: {total}%")
print(f"Average: {average}%")

# Check if average is high
if average > 60:
    print("⚠️ Warning: High resource usage!")
```

---

### Exercise 4: Data Types Practice

Create `exercise4.py`:

```python
# Exercise 4: Work with different types
app_name = "DevOps Monitor"
version = 1.5
total_servers = 25
is_production = True
uptime_days = 30

# Print with types
print(f"App: {app_name} (type: {type(app_name).__name__})")
print(f"Version: {version} (type: {type(version).__name__})")
print(f"Servers: {total_servers} (type: {type(total_servers).__name__})")
print(f"Production: {is_production} (type: {type(is_production).__name__})")
print(f"Uptime: {uptime_days} days")
```

---

## Common Mistakes

### Mistake 1: Undefined Variable
```python
# ❌ Wrong - using variable before defining
print(server_name)
server_name = "web-1"

# ✅ Correct - define first, use later
server_name = "web-1"
print(server_name)
```

### Mistake 2: Mixing Types
```python
# ❌ Wrong - can't add string and number
result = "Server" + 5

# ✅ Correct - convert number to string
result = "Server" + str(5)
# or use f-string
result = f"Server{5}"
```

### Mistake 3: Variable Name Typos
```python
# ❌ Wrong - typo in variable name
server_name = "web-1"
print(servername)  # Error! Missing underscore

# ✅ Correct - exact same name
server_name = "web-1"
print(server_name)
```

---

## Type Conversion

```python
# String to Integer
cpu_str = "75"
cpu_int = int(cpu_str)
print(cpu_int + 10)  # 85

# Integer to String
port = 8080
port_str = str(port)
print("Port: " + port_str)

# String to Float
memory_str = "60.5"
memory_float = float(memory_str)
print(memory_float)  # 60.5

# Float to Integer (removes decimal)
cpu = 75.8
cpu_int = int(cpu)
print(cpu_int)  # 75
```

---

## Challenge: Build a Server Info Card

Create `challenge.py`:

```python
# Challenge: Create a detailed server info card

# Server details
hostname = "prod-web-server-01"
ip = "192.168.100.50"
os = "Ubuntu 22.04 LTS"
cpu_cores = 8
ram_gb = 32.0
disk_tb = 2.5
uptime_days = 45
is_healthy = True

# Calculate some stats
ram_mb = ram_gb * 1024
disk_gb = disk_tb * 1024

# Print beautiful card
print("╔" + "═" * 48 + "╗")
print("║" + " " * 15 + "SERVER INFO CARD" + " " * 17 + "║")
print("╠" + "═" * 48 + "╣")
print(f"║ Hostname: {hostname:35} ║")
print(f"║ IP Address: {ip:33} ║")
print(f"║ Operating System: {os:27} ║")
print("╠" + "═" * 48 + "╣")
print(f"║ CPU Cores: {cpu_cores:34} ║")
print(f"║ RAM: {ram_gb} GB ({ram_mb} MB){' ' * 19} ║")
print(f"║ Disk: {disk_tb} TB ({disk_gb} GB){' ' * 17} ║")
print("╠" + "═" * 48 + "╣")
print(f"║ Uptime: {uptime_days} days{' ' * 29} ║")
print(f"║ Health Status: {'✅ Healthy' if is_healthy else '❌ Unhealthy':26} ║")
print("╚" + "═" * 48 + "╝")
```

---

## What You Learned Today

✅ Variables store information  
✅ Four main data types: string, int, float, bool  
✅ How to check types with `type()`  
✅ String formatting with f-strings  
✅ Type conversion between different types  
✅ Best practices for variable names  

---

## Tomorrow's Preview

**Day 3: User Input and String Operations**
- Getting input from users
- String methods (upper, lower, strip, etc.)
- Building interactive scripts

---

## Homework

1. ✅ Complete all 4 exercises
2. ✅ Try the challenge
3. ✅ Experiment with different data types
4. ✅ Create your own server info script

**Great work on Day 2! See you tomorrow! 🚀**
