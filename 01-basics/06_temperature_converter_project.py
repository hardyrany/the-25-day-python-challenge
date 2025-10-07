# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 18:23:01 2025

@author: HardyR
"""

FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
OFFSET = 32

# User input
celsius_input = 20
fahrenheit_input = 85

# Conversions
converted_to_f = (celsius_input * FAHRENHEIT_TO_CELSIUS) + OFFSET
converted_to_c = (fahrenheit_input * CELSIUS_TO_FAHRENHEIT) + OFFSET

# Display
print(f"{celsius_input}°C -> {converted_to_f:.1f}°F")
print(f"{fahrenheit_input}°C -> {converted_to_c:.1f}°C")
