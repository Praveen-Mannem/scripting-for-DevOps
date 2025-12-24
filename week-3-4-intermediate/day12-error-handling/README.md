# Day 12: Error Handling (try/except)

## 📚 Learning Objectives
- Handle errors gracefully with try/except
- Use multiple except blocks
- Implement finally blocks
- Raise custom exceptions

## 🎯 Why This Matters for DevOps
Error handling prevents scripts from crashing and allows for:
- Graceful failure recovery
- Meaningful error messages
- Logging failures
- Retry mechanisms
- Production-ready scripts

---

## 📖 Concepts

### 1. Basic try/except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### 2. Multiple Exceptions
```python
try:
    file = open('config.txt', 'r')
    value = int(file.read())
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid number format")
```

### 3. Finally Block
```python
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # Always executes
    print("Cleanup complete")
```

### 4. Raising Exceptions
```python
def check_port(port):
    if port < 1 or port > 65535:
        raise ValueError("Port must be between 1 and 65535")
    return port
```

---

## 💻 Practice Exercises

### Exercise 1: Safe File Reader
**File:** `safe_file_reader.py`

### Exercise 2: Connection Retry Handler
**File:** `connection_retry.py`

### Exercise 3: Input Validator
**File:** `input_validator.py`

---

## ⏭️ Next Steps
Tomorrow: Day 13 - Modules and Packages
