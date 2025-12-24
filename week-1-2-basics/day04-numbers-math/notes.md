# Day 4: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **Number types**: int (whole numbers) and float (decimals)
2. **Math operators**: +, -, *, /, //, %, **
3. **Math module**: ceil, floor, sqrt, abs
4. **Type conversion**: int(), float(), str()

## Math Operators Cheatsheet
```python
10 + 5    # 15  (addition)
10 - 5    # 5   (subtraction)
10 * 5    # 50  (multiplication)
10 / 5    # 2.0 (division - returns float)
10 // 3   # 3   (floor division - rounds down)
10 % 3    # 1   (modulus - remainder)
10 ** 2   # 100 (exponent - power)
```

## Common Math Functions
```python
import math

round(4.567, 2)   # 4.57 (round to 2 decimals)
math.ceil(4.2)    # 5 (round up)
math.floor(4.8)   # 4 (round down)
math.sqrt(16)     # 4.0 (square root)
abs(-10)          # 10 (absolute value)
```

## DevOps Use Cases
- **Disk space**: Calculate usage percentages
- **Uptime**: Convert between time units
- **Metrics**: Calculate averages, min, max
- **Thresholds**: Check if values exceed limits

## Questions/Confusion
- 
- 

## Practice Summary
- [ ] Completed disk_calculator.py
- [ ] Completed uptime_calculator.py
- [ ] Completed performance_metrics.py
- [ ] Experimented with math operations

## Real-World Example
```python
# Calculate if server needs more memory
total_memory = 16  # GB
used_memory = 14   # GB
usage_percent = (used_memory / total_memory) * 100

if usage_percent > 85:
    print("⚠️  Consider adding more memory")
```

## Tomorrow's Preview
Day 5: Lists - Learn to work with collections of data
