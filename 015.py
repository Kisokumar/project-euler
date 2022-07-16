# Problem 15 - Lattice Paths
# How many routes are there through a 20x20 grid from the top left to the bottom right.

def factorial(n):
    for i in range(n-1,0,-1):
        n*=i
    return n

def binomCoefficient(i,j):
    return int(factorial(i)/(factorial(j)*factorial(i-j)))

if __name__ == '__main__':
    print(binomCoefficient(40,20))

# ans = 0
