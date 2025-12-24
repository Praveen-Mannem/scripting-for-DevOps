# Day 3: User Input and String Operations

## 📚 Learning Objectives
- Get input from users
- Work with strings
- Format output nicely
- Build interactive scripts

## 🎯 Why This Matters for DevOps
In real DevOps scenarios, you'll often need to:
- Get server names from users
- Ask for confirmation before dangerous operations
- Collect configuration details
- Build interactive deployment scripts

---

## 📖 Concepts

### 1. Getting User Input
```python
# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input is always a string
age = input("Enter your age: ")  # This is a string!
age = int(age)  # Convert to number
```

### 2. String Operations
```python
text = "DevOps Engineer"

# Common operations
print(text.upper())      # DEVOPS ENGINEER
print(text.lower())      # devops engineer
print(text.replace("DevOps", "Cloud"))  # Cloud Engineer
print(len(text))         # 15

# String methods
print(text.startswith("Dev"))  # True
print(text.endswith("er"))     # True
print(text.split())            # ['DevOps', 'Engineer']
```

### 3. String Formatting
```python
name = "Alice"
role = "DevOps"

# f-strings (modern way)
print(f"{name} is a {role} engineer")

# format() method
print("{} is a {} engineer".format(name, role))

# Old way (still works)
print("%s is a %s engineer" % (name, role))
```

### 4. Multi-line Strings
```python
message = """
This is a
multi-line
string
"""
```

---

## 💻 Practice Exercises

### Exercise 1: Server Information Collector
Create a script that collects server details from the user.

**File:** `server_info.py`

### Exercise 2: Log Message Formatter
Build a script that formats log messages with timestamps.

**File:** `log_formatter.py`

### Exercise 3: Deployment Confirmation
Create a script that asks for confirmation before deployment.

**File:** `deploy_confirm.py`

---

## 🔨 Hands-On Tasks

1. Run all example scripts
2. Complete all exercises
3. Experiment with different string methods
4. Try the challenge exercise

---

## 🎓 Key Takeaways
- `input()` always returns a string
- Convert input using `int()`, `float()`, etc.
- f-strings are the modern way to format strings
- String methods are powerful for text manipulation

---

## 📝 Notes
- Always validate user input in real scripts
- Use `.strip()` to remove extra whitespace
- Check if input is empty before processing
- Handle conversion errors (we'll learn this in error handling)

---

## ⏭️ Next Steps
Tomorrow: Day 4 - Numbers and Math Operations
