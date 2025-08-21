"""
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""

Tsum = 0

for i in range(1, 51):
        Tsum += i

print(f"The sum of integers from 1 to 50 is: {Tsum}")
