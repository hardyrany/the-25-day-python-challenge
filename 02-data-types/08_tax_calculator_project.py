# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:13:21 2025

@author: HardyR
"""

base_income: float = float(input("Enter your yearly income: "))
tax_rate: float = float(input("Enter your tax percentage: ")) / 100
taxed: float = base_income * tax_rate

print("=" * 40)
print("Income Tax Calculator")
print("=" * 40)
print(f"Base income:          ${base_income:.2f}")
print(f"Tax rate:             {tax_rate:.0%}")
print("-" * 40)
print(f"Yearly tax (Base):    {taxed:.2f}")
print("=" * 40)
