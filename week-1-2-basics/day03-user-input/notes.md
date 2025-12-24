# Day 3: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **input() function**: Gets text from user
2. **String methods**: upper(), lower(), strip(), replace(), etc.
3. **f-strings**: Modern way to format strings
4. **Type conversion**: Converting strings to numbers

## Common String Methods Cheatsheet
```python
text = "  Hello World  "

text.upper()          # "  HELLO WORLD  "
text.lower()          # "  hello world  "
text.strip()          # "Hello World"
text.replace("H", "J") # "  Jello World  "
text.split()          # ["Hello", "World"]
len(text)             # 15
text.startswith("H")  # False (has spaces!)
text.strip().startswith("H")  # True
```

## DevOps Use Cases
- **User input**: Getting server names, IP addresses, confirmation
- **String manipulation**: Parsing log files, formatting output
- **Validation**: Checking if input matches expected format

## Questions/Confusion
- 
- 

## Practice Summary
- [ ] Completed server_info.py
- [ ] Completed log_formatter.py
- [ ] Completed deploy_confirm.py
- [ ] Experimented with string methods

## Real-World Example
```python
# A simple script to collect AWS instance details
instance_id = input("Enter EC2 instance ID: ")
region = input("Enter AWS region: ")

print(f"\nConnecting to instance {instance_id} in {region}...")
```

## Tomorrow's Preview
Day 4: Numbers and Math Operations - Learn to work with numbers for calculations
