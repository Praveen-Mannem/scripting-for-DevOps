# Day 4: Numbers and Math Operations

## 📚 Learning Objectives
- Work with different number types
- Perform mathematical operations
- Use Python's math module
- Handle numeric calculations in scripts

## 🎯 Why This Matters for DevOps
DevOps engineers constantly work with numbers:
- Calculate disk space usage percentages
- Monitor CPU and memory metrics
- Calculate uptime and availability
- Process performance statistics
- Handle time calculations

---

## 📖 Concepts

### 1. Number Types
```python
# Integers (whole numbers)
servers = 10
port = 8080

# Floats (decimal numbers)
cpu_usage = 75.5
memory_gb = 16.0

# Type conversion
num_str = "100"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float
```

### 2. Basic Math Operations
```python
# Basic operators
print(10 + 5)   # 15 (addition)
print(10 - 5)   # 5  (subtraction)
print(10 * 5)   # 50 (multiplication)
print(10 / 5)   # 2.0 (division - always returns float)
print(10 // 3)  # 3  (floor division - rounds down)
print(10 % 3)   # 1  (modulus - remainder)
print(10 ** 2)  # 100 (exponent - power)
```

### 3. Math Module
```python
import math

# Useful functions
print(math.ceil(4.2))   # 5 (round up)
print(math.floor(4.8))  # 4 (round down)
print(round(4.567, 2))  # 4.57 (round to 2 decimals)
print(math.sqrt(16))    # 4.0 (square root)
print(abs(-10))         # 10 (absolute value)
```

### 4. Practical Calculations
```python
# Calculate percentage
total_disk = 500  # GB
used_disk = 375   # GB
percentage = (used_disk / total_disk) * 100
print(f"Disk usage: {percentage}%")

# Calculate average
cpu_readings = [45, 67, 89, 56, 72]
average = sum(cpu_readings) / len(cpu_readings)
print(f"Average CPU: {average}%")
```

---

## 💻 Practice Exercises

### Exercise 1: Disk Space Calculator
Calculate disk space usage and available space.

**File:** `disk_calculator.py`

### Exercise 2: Server Uptime Calculator
Calculate server uptime in different units.

**File:** `uptime_calculator.py`

### Exercise 3: Performance Metrics
Calculate average, min, max from performance data.

**File:** `performance_metrics.py`

---

## 🔨 Hands-On Tasks

1. Run all example scripts
2. Complete all exercises
3. Experiment with different math operations
4. Try the challenge exercise

---

## 🎓 Key Takeaways
- Python has two number types: int and float
- Division (/) always returns a float
- Use // for integer division
- Use % to get remainder
- Import math module for advanced operations

---

## 📝 Notes
- Always check for division by zero
- Round floating point numbers for display
- Use appropriate number types (int vs float)
- Convert user input to numbers before calculations

---

## ⏭️ Next Steps
Tomorrow: Day 5 - Lists and Collections
