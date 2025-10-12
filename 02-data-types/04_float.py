# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 14:29:45 2025

@author: HardyR
"""

rate: float = 5.5
percent: float = 0.43
PI: float = 3.1415
balance: int = 5000
rate: float = 5.35
interest: float = balance * (rate / 100)
new_balance: float = balance + interest
print(f"Ballance: ${balance}")
print(f"After interest: ${new_balance}")


a: float = 0.1
b: float = 0.2
print(f"{a} + {b} = {a + b}")
print(a + b == 0.3)

a: float = 0.1
b: float = 0.2
sum: float = round(a + b, 1)
print(sum == 0.3)

a: float = 0.1111
b: float = 0.2222
sum: float = round(a + b, 2)
print(sum)

big_float: float = 0.123_456_789
print(big_float)
