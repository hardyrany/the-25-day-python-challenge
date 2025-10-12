# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:13:21 2025

@author: HardyR
"""

# Get user input and calculate tax
base_income: float = float(input("Enter your yearly income: "))
double_income: float = base_income * 2
triple_income: float = base_income * 3

# Calculated tax
tax_rate: float = float(input("Enter your tax percentage: ")) / 100
taxed: float = base_income * tax_rate
double_tax: float = double_income * tax_rate
triple_tax: float = triple_income * tax_rate

# Display results
print("=" * 40)
print("Income Tax Calculator")
print("=" * 40)
print(f"Base income:          ${base_income:.2f}")
print(f"Base income(doubled): ${double_income:.2f}")
print(f"Base income(tripled): ${triple_income:.2f}")
print(f"Tax rate:             {tax_rate:.0%}")
print("-" * 40)
print(f"Yearly tax (Base):    {taxed:.2f}")
print(f"Yearly tax (Doubled): {double_tax:.2f}")
print(f"Yearly tax (Tripled): {triple_tax:.2f}")
print("=" * 40)
