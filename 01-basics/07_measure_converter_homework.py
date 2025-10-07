# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 18:42:06 2025

@author: HardyR
"""

# Conversion constants
MILES_TO_KM = 1.60934
KM_TO_MILES = 0.621371

# Convert miles to kilometers
miles_input = float(input("What miles? "))
converted_to_k = MILES_TO_KM * miles_input
print(f"{converted_to_k:.2f} kilometers")


# Convert kilometers to miles
kilometers_input = float(input("What kilometers? "))
converted_to_m = KM_TO_MILES * kilometers_input
print(f"{converted_to_m:.2f} miles")
