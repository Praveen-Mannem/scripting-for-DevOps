# Day 7: Conditional Statements (if/elif/else)

## 📚 Learning Objectives
- Use if/elif/else statements
- Compare values with operators
- Combine conditions with and/or
- Make decisions in scripts

## 🎯 Why This Matters for DevOps
Conditionals are essential for:
- Checking server status before actions
- Validating input before processing
- Handling different environments (dev/staging/prod)
- Alert thresholds (CPU > 80%, disk > 90%)
- Error handling and recovery

---

## 📖 Concepts

### 1. Basic if Statement
```python
cpu_usage = 85

if cpu_usage > 80:
    print("⚠️ High CPU usage!")
```

### 2. if-else Statement
```python
status = "running"

if status == "running":
    print("✓ Server is healthy")
else:
    print("✗ Server is down")
```

### 3. if-elif-else Statement
```python
disk_usage = 75

if disk_usage < 70:
    print("✓ Disk usage is healthy")
elif disk_usage < 85:
    print("⚠️ Disk usage is moderate")
else:
    print("🚨 Disk usage is critical!")
```

### 4. Comparison Operators
```python
# Equal to
if port == 80:
    print("HTTP port")

# Not equal to
if status != "running":
    print("Server not running")

# Greater than, less than
if cpu > 80:
    print("High CPU")
if memory < 20:
    print("Low memory")

# Greater/less than or equal
if uptime >= 99.9:
    print("Meeting SLA")
```

### 5. Logical Operators
```python
# AND - both must be true
if cpu > 80 and memory > 80:
    print("System overloaded")

# OR - at least one must be true
if port == 80 or port == 443:
    print("Web server port")

# NOT - reverse the condition
if not is_backup_enabled:
    print("Backups disabled!")
```

---

## 💻 Practice Exercises

### Exercise 1: Server Health Checker
**File:** `health_checker.py`

### Exercise 2: Environment Validator
**File:** `env_validator.py`

### Exercise 3: Alert System
**File:** `alert_system.py`

---

## ⏭️ Next Steps
Tomorrow: Day 8 - Loops (for and while)
