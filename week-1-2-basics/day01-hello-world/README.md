# Day 1: Getting Started with Python

Welcome to your first day of learning Python for DevOps! 🎉

## Learning Objectives

By the end of today, you will:
- ✅ Understand what Python is and why it's used in DevOps
- ✅ Write and run your first Python script
- ✅ Use print statements to display information
- ✅ Add comments to your code

---

## What is Python?

Python is a **programming language** that's:
- **Easy to read** - Code looks like English
- **Powerful** - Used by Google, Netflix, NASA
- **Versatile** - Web apps, automation, AI, DevOps
- **Popular** - Huge community and lots of help available

## Why Python for DevOps?

DevOps engineers use Python to:
- 🤖 **Automate repetitive tasks** (backups, deployments)
- 📊 **Monitor servers** (CPU, memory, disk usage)
- 📝 **Analyze logs** (find errors, patterns)
- 🔧 **Manage infrastructure** (AWS, Azure, Docker, Kubernetes)
- 🚀 **Build CI/CD pipelines** (automated testing, deployment)

---

## Your First Python Script

### Step 1: Create a Python File

Create a file called `hello.py` in this folder.

### Step 2: Write Your First Code

Open `hello.py` and type:

```python
# My first Python script
print("Hello, DevOps World!")
```

### Step 3: Run Your Script

Open terminal/PowerShell in this folder and run:

```bash
python hello.py
```

You should see:
```
Hello, DevOps World!
```

**🎉 Congratulations! You just wrote and ran your first Python script!**

---

## Understanding the Code

### Comments (`#`)

```python
# This is a comment - Python ignores this line
# Comments help explain what your code does
```

**Why use comments?**
- Explain complex code
- Leave notes for yourself
- Help others understand your code

### Print Statement

```python
print("Hello, World!")
```

The `print()` function displays text on the screen.

**Syntax:**
- `print()` - the function name
- `"..."` - text inside quotes (called a "string")
- Text must be inside quotes: `"` or `'`

---

## Practice Exercises

### Exercise 1: Multiple Print Statements

Create `exercise1.py` and write:

```python
# Exercise 1: Multiple prints
print("Hello, DevOps World!")
print("My name is Praveen")
print("I'm learning Python for DevOps")
```

**Run it:**
```bash
python exercise1.py
```

**Expected Output:**
```
Hello, DevOps World!
My name is Praveen
I'm learning Python for DevOps
```

---

### Exercise 2: Print Server Information

Create `exercise2.py` and write:

```python
# Exercise 2: Server information
print("=== Server Status Report ===")
print("Server Name: web-server-1")
print("IP Address: 192.168.1.10")
print("Status: Running")
print("CPU Usage: 45%")
print("Memory Usage: 60%")
print("===========================")
```

**Run it and see the output!**

---

### Exercise 3: Create Your Own

Create `exercise3.py` and write a script that prints:
- Your name
- Your city
- Why you want to learn DevOps
- Your goal for this course

**Example:**
```python
# Exercise 3: About me
print("Name: Praveen")
print("City: Bangalore")
print("Goal: Become a DevOps Engineer")
print("Why: I want to automate everything!")
```

---

## Common Mistakes (and How to Fix Them)

### Mistake 1: Forgetting Quotes
```python
# ❌ Wrong
print(Hello)

# ✅ Correct
print("Hello")
```

### Mistake 2: Typo in print
```python
# ❌ Wrong
prit("Hello")  # Typo!

# ✅ Correct
print("Hello")
```

### Mistake 3: Mismatched Quotes
```python
# ❌ Wrong
print("Hello')

# ✅ Correct
print("Hello")
# or
print('Hello')
```

---

## Quick Reference

### Print Statement
```python
print("Your text here")
print('Single quotes work too')
```

### Comments
```python
# Single line comment

# You can have multiple
# comment lines
```

### Running Python Scripts
```bash
# In terminal/PowerShell
python filename.py
```

---

## Challenge: Build a DevOps Banner

Create `challenge.py` that prints a nice banner for a DevOps tool:

```python
# Challenge: DevOps Banner
print("*" * 40)
print("*" + " " * 38 + "*")
print("*     DEVOPS AUTOMATION TOOL v1.0     *")
print("*" + " " * 38 + "*")
print("*" * 40)
print()
print("Status: All systems operational")
print("Servers monitored: 25")
print("Uptime: 99.9%")
```

**Hint:** The `*` character repeated makes a nice border!

---

## What You Learned Today

✅ What Python is and why it's important for DevOps  
✅ How to write and run Python scripts  
✅ How to use `print()` to display information  
✅ How to add comments to explain your code  
✅ Common mistakes and how to avoid them  

---

## Next Steps

Tomorrow (Day 2), you'll learn about:
- **Variables** - Storing information
- **Data types** - Different kinds of data
- **Using variables** in print statements

---

## Homework

1. ✅ Complete all 3 exercises
2. ✅ Try the challenge
3. ✅ Experiment - try printing different things!
4. ✅ Make mistakes and fix them (that's how you learn!)

---

## Tips for Success

💡 **Type the code yourself** - Don't copy-paste  
💡 **Run every example** - See what happens  
💡 **Experiment** - Change things and see what breaks  
💡 **Make mistakes** - They're the best teachers  
💡 **Have fun** - Programming should be enjoyable!  

---

**Great job on Day 1! See you tomorrow! 🚀**
