# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 22:22:41 2025

@author: HardyR
"""

## Primitive Types

# String
text: str = "This is text"
# Integer
number: int = 42
# Float Point Numbers
decimal: float = 4.5
# Complex Numbers
imaginary: complex = 1 + 2j
# Booleans
is_connected: bool = True
is_not_connected: bool = False

# Collections Types:
# Lists
list_string: list[str] = ["Bob", "James", "Sandra"]
list_number: list[int] = [20, 10, 15, 45]
list_mix: list = ["Bob", 20, True, False]

# Tuples
tuple_numbers: tuple[int, int] = (1, 2)
point: tuple[float, float] = (1.5, 2.5)
tuple_string: tuple[str, str, str] = ("Banana", "Orange", "Mango")

# Sets
unique: set[int] = {1, 2, 4, 8, 3, 6, 9, 5}
string_set: set[str] = {"Banana", "Orange", "Mango"}

# Frozen Sets
frozen: frozenset[int] = frozenset({1, 2, 4, 8, 3, 6, 9, 5})
frozen_string: frozenset[str] = frozenset({"Banana", "Orange", "Mango"})

# Dictionaries
users: dict[str, int] = {"Bob": 0, "James": 1, "Sandra": 2}
dict_srt_string: dict[str, str] = {"Bob": "Dylan", "James": "Bond", "Sandra": "Katrina"}
dict_int_integer: dict[int, int] = {20: 10, 30: 15, 50: 25}

# None
user_selected: str | None = None
number_selected: int | None = None


print(text)
print(number)
print(decimal)
print(imaginary)
print(is_connected)
print(is_not_connected)
print(list_string)
print(list_number)
print(list_mix)
print(tuple_numbers)
print(point)
print(tuple_string)
print(unique)
print(string_set)
print(frozen)
print(frozen_string)
print(users)
print(dict_srt_string)
print(dict_int_integer)
print(user_selected)
print(number_selected)
