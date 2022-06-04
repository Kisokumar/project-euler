# Problem 3 - Largest Prime Factor
# Largest prime factor of 600851475143

import math

def sol(x):
    i = 2
    while i * i < x:
        while x % i == 0:
            x = x / i
        i = i + 1

    return x 

print(sol(600851475143))

# ans = 6857
