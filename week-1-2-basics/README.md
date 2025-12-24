# Week 1-2 Complete Materials

This folder contains all learning materials for Week 1-2: Python Basics

## Daily Lessons

### ✅ Day 1: Hello World (COMPLETE)
- Location: `day01-hello-world/`
- Topics: Print statements, comments, running Python
- Exercises: 3 exercises + 1 challenge

### Day 2: Variables and Data Types
- Location: `day02-variables/`
- Topics: Variables, strings, integers, floats, booleans
- Exercises: Create server info scripts

### Day 3: User Input and Strings
- Topics: input(), string methods, f-strings
- Exercises: Interactive server configuration

### Day 4: Numbers and Math
- Topics: Math operations, calculations, comparisons
- Exercises: Resource usage calculator

### Day 5: Lists
- Topics: Creating lists, accessing items, list methods
- Exercises: Server inventory management

### Day 6: Dictionaries
- Topics: Key-value pairs, nested data, JSON-like structures
- Exercises: Server configuration management

### Day 7: Conditions
- Topics: if/elif/else, comparison operators, logical operators
- Exercises: Server health checker

### Day 8: Loops
- Topics: for loops, while loops, break/continue
- Exercises: Multi-server monitoring

### Day 9-10: Functions
- Topics: Defining functions, parameters, return values
- Exercises: Reusable DevOps utilities

### Week Project: Server Monitoring Dashboard
- Location: `project-server-monitor/`
- Build a complete monitoring dashboard
- Combine all week's concepts

---

## Quick Code Reference

### Variables
```python
server_name = "web-1"
cpu_usage = 75
is_running = True
```

### User Input
```python
name = input("Enter server name: ")
print(f"Checking {name}...")
```

### Lists
```python
servers = ["web-1", "db-1", "app-1"]
for server in servers:
    print(server)
```

### Dictionaries
```python
server = {
    "name": "web-1",
    "ip": "192.168.1.10",
    "cpu": 45
}
print(server["name"])
```

### Conditions
```python
if cpu > 80:
    print("High")
elif cpu > 50:
    print("Medium")
else:
    print("Low")
```

### Functions
```python
def check_health(cpu, memory):
    if cpu > 80 or memory > 80:
        return "CRITICAL"
    return "OK"
```

---

## All Exercise Files

Each day includes:
- `README.md` - Lesson content
- `exercise1.py` - Basic practice
- `exercise2.py` - Intermediate practice
- `exercise3.py` - Advanced practice
- `challenge.py` - Optional challenge

---

## Learning Path

1. Read the README.md in each day's folder
2. Type out the examples (don't copy-paste!)
3. Run the code and see the output
4. Complete all exercises
5. Try the challenge
6. Move to next day

---

## Tips

- Practice daily for 1-2 hours
- Don't rush - understand each concept
- Make mistakes and fix them
- Ask questions when stuck
- Have fun! 🚀
