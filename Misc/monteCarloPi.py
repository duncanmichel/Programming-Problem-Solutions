"""
Monte Carlo simulation to estimate the value of Pi
"""

#code
from random import random
max_interval = int(input())
circle_count = 0
square_count = 0
for interval in range(max_interval):
    x = random()
    y = random()
    d = x*x + y*y
    if d <= 1:
        circle_count += 1
    square_count += 1
print("pi is ",4*(circle_count/square_count))
