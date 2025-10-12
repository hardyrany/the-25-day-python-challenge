# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 21:59:12 2025

@author: HardyR
"""

# Type anotation

# String value assigned to string-annotated variable
name: str = "Bob"
# Integer value assigned to integer-annotated variable
age: int = 30

print(name)
print(age)

# Integer value assigned to string-annotated variable / Type mismatch but works
name: str = 100
# String value assigned to integer-annotated variable / Type mismatch but works
age: int = "42"

print(name)
print(age)

# String value assigned to integer-annotated variable / Type mismatch
a: int = "10"
b: int = "20"
print(f"The sum of {a} + {b} is {a + b}")

# Integer value assigned to integer-annotated variable / Type match
a: int = 10
b: int = 20
print(f"The sum of {a} + {b} is {a + b}")
