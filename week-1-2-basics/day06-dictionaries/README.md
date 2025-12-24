# Day 6: Dictionaries - Key-Value Pairs

## 📚 Learning Objectives
- Create and use dictionaries
- Access and modify dictionary data
- Iterate through dictionaries
- Use dictionaries for structured data

## 🎯 Why This Matters for DevOps
Dictionaries are perfect for:
- Server configurations
- Environment variables
- API responses (JSON data)
- System information
- User credentials and settings

---

## 📖 Concepts

### 1. Creating Dictionaries
```python
# Empty dictionary
server = {}

# Dictionary with data
server = {
    "name": "web-server-01",
    "ip": "192.168.1.10",
    "port": 8080,
    "status": "running"
}
```

### 2. Accessing Values
```python
server = {"name": "web-01", "ip": "192.168.1.10", "port": 80}

# Access by key
print(server["name"])      # web-01
print(server.get("ip"))    # 192.168.1.10

# get() is safer (returns None if key doesn't exist)
print(server.get("cpu"))   # None
print(server.get("cpu", "N/A"))  # N/A (default value)
```

### 3. Modifying Dictionaries
```python
server = {"name": "web-01", "status": "stopped"}

# Add/Update
server["status"] = "running"  # Update existing
server["cpu"] = 45.5          # Add new key

# Remove
del server["cpu"]             # Delete key
server.pop("status")          # Remove and return value
server.clear()                # Remove all
```

### 4. Dictionary Methods
```python
server = {"name": "web-01", "ip": "192.168.1.10", "port": 80}

# Get all keys, values, items
print(server.keys())          # dict_keys(['name', 'ip', 'port'])
print(server.values())        # dict_values(['web-01', '192.168.1.10', 80])
print(server.items())         # dict_items([('name', 'web-01'), ...])

# Check if key exists
if "name" in server:
    print("Name exists")

# Loop through dictionary
for key, value in server.items():
    print(f"{key}: {value}")
```

---

## 💻 Practice Exercises

### Exercise 1: Server Configuration Manager
**File:** `server_config.py`

### Exercise 2: Environment Variables Handler
**File:** `env_manager.py`

### Exercise 3: System Info Collector
**File:** `system_info.py`

---

## ⏭️ Next Steps
Tomorrow: Day 7 - Conditional Statements (if/elif/else)
