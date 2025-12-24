# Day 5: Lists - Working with Collections

## 📚 Learning Objectives
- Create and manipulate lists
- Access list elements
- Use list methods
- Iterate through lists

## 🎯 Why This Matters for DevOps
Lists are everywhere in DevOps:
- Store multiple server names
- Collect log entries
- Manage IP addresses
- Track deployment steps
- Handle multiple configuration values

---

## 📖 Concepts

### 1. Creating Lists
```python
# Empty list
servers = []

# List with items
servers = ["web1", "web2", "db1"]
ports = [80, 443, 8080, 3000]
mixed = ["server1", 8080, True, 3.14]
```

### 2. Accessing Elements
```python
servers = ["web1", "web2", "db1", "cache1"]

# Index starts at 0
print(servers[0])   # web1 (first item)
print(servers[2])   # db1 (third item)
print(servers[-1])  # cache1 (last item)
print(servers[-2])  # db1 (second from end)

# Slicing
print(servers[1:3])   # ['web2', 'db1']
print(servers[:2])    # ['web1', 'web2']
print(servers[2:])    # ['db1', 'cache1']
```

### 3. List Methods
```python
servers = ["web1", "web2"]

# Add items
servers.append("db1")        # Add to end
servers.insert(1, "cache1")  # Insert at position
servers.extend(["api1", "api2"])  # Add multiple

# Remove items
servers.remove("web1")  # Remove by value
servers.pop()           # Remove last item
servers.pop(0)          # Remove by index
servers.clear()         # Remove all

# Other operations
print(len(servers))     # Get length
print("web1" in servers)  # Check if exists
servers.sort()          # Sort alphabetically
servers.reverse()       # Reverse order
```

### 4. List Comprehension (Bonus)
```python
# Create list from range
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = [x * 2 for x in numbers]
# Result: [2, 4, 6, 8, 10]

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
# Result: [2, 4]
```

---

## 💻 Practice Exercises

### Exercise 1: Server Manager
Manage a list of servers with add/remove operations.

**File:** `server_manager.py`

### Exercise 2: Port Scanner Simulator
Work with a list of ports to scan.

**File:** `port_scanner.py`

### Exercise 3: Log Entry Collector
Collect and display log entries.

**File:** `log_collector.py`

---

## 🎓 Key Takeaways
- Lists store multiple items in order
- Index starts at 0
- Negative indices count from the end
- Lists are mutable (can be changed)
- Many built-in methods available

---

## ⏭️ Next Steps
Tomorrow: Day 6 - Dictionaries (Key-Value Pairs)
