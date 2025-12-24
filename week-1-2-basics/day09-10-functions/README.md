# Day 9-10: Functions - Reusable Code Blocks

## 📚 Learning Objectives
- Define and call functions
- Use parameters and arguments
- Return values from functions
- Understand function scope
- Create modular, reusable code

## 🎯 Why This Matters for DevOps
Functions are essential for:
- Reusing code across scripts
- Organizing complex automation
- Creating utility libraries
- Making code maintainable
- Reducing errors and duplication

---

## 📖 Concepts

### 1. Basic Functions
```python
# Define a function
def greet():
    print("Hello, DevOps!")

# Call the function
greet()  # Output: Hello, DevOps!
```

### 2. Functions with Parameters
```python
# Function with one parameter
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # Hello, Alice!

# Function with multiple parameters
def check_server(name, status):
    print(f"Server {name} is {status}")

check_server("web-01", "running")
```

### 3. Return Values
```python
# Return a value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8

# Return multiple values
def get_server_info():
    name = "web-01"
    ip = "192.168.1.10"
    return name, ip

server_name, server_ip = get_server_info()
```

### 4. Default Parameters
```python
def deploy(app_name, environment="dev"):
    print(f"Deploying {app_name} to {environment}")

deploy("myapp")              # Uses default: dev
deploy("myapp", "prod")      # Uses provided: prod
```

### 5. Docstrings (Documentation)
```python
def calculate_uptime(total_hours, downtime_hours):
    """
    Calculate server uptime percentage.
    
    Args:
        total_hours: Total hours in period
        downtime_hours: Hours of downtime
        
    Returns:
        Uptime percentage as float
    """
    uptime = ((total_hours - downtime_hours) / total_hours) * 100
    return uptime
```

---

## 💻 Practice Exercises

### Exercise 1: Server Management Functions
**File:** `server_functions.py`

### Exercise 2: Monitoring Utilities
**File:** `monitoring_utils.py`

### Exercise 3: Deployment Helper
**File:** `deployment_helper.py`

---

## ⏭️ Next Steps
Week 3-4: Intermediate Python Topics
