# Day 8: Loops (for and while)

## 📚 Learning Objectives
- Use for loops to iterate
- Use while loops for conditions
- Control loop flow with break/continue
- Loop through lists and dictionaries

## 🎯 Why This Matters for DevOps
Loops are critical for:
- Processing multiple servers
- Iterating through log files
- Monitoring multiple services
- Batch operations
- Repeating tasks until completion

---

## 📖 Concepts

### 1. For Loops
```python
# Loop through a list
servers = ["web1", "web2", "db1"]
for server in servers:
    print(f"Checking {server}...")

# Loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Loop with range (start, stop)
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# Loop with enumerate (get index)
for index, server in enumerate(servers):
    print(f"{index}: {server}")
```

### 2. While Loops
```python
# Loop while condition is true
count = 0
while count < 5:
    print(count)
    count += 1

# Loop until user input
retry = True
while retry:
    status = input("Check again? (yes/no): ")
    if status == "no":
        retry = False
```

### 3. Loop Control
```python
# break - exit loop
for i in range(10):
    if i == 5:
        break  # Stop at 5
    print(i)

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)
```

### 4. Loop Through Dictionaries
```python
server = {"name": "web1", "ip": "192.168.1.10", "port": 80}

# Loop through keys
for key in server:
    print(key)

# Loop through values
for value in server.values():
    print(value)

# Loop through key-value pairs
for key, value in server.items():
    print(f"{key}: {value}")
```

---

## 💻 Practice Exercises

### Exercise 1: Multi-Server Monitor
**File:** `multi_server_monitor.py`

### Exercise 2: Log File Processor
**File:** `log_processor.py`

### Exercise 3: Retry Mechanism
**File:** `retry_mechanism.py`

---

## ⏭️ Next Steps
Tomorrow: Day 9-10 - Functions
