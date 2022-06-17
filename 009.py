# Probelm 9 - Special Pythagorean triplet
# Find the product of the pythagorean triplet where a+b+c=1000

import math

def isSquare(n):
    """Checks if n is a square number and returns a boolean value"""
    return math.sqrt(n).is_integer()

def sol():
    """O(n^2) time complexity, loops over a,b 1000 times each"""
    for a in range(1000):
        for b in range(1000):
            cSquared = ((a**2)+(b**2))
            c = math.sqrt(cSquared)
            if isSquare(cSquared):
                if int(a+b+c)==1000:
                    print(int(a*b*c))

if __name__ == '__main__':
    sol()

# ans = 31875000
