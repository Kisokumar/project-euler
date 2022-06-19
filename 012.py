# Problem 12 - Highly divisible triangular number
# Return the first triangle number with over five hundred divisors

from functools import reduce

def factorsFast(n):    
    return set(reduce(list.__add__, 
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factorsSlow(n):
    factors = []
    for i in range(1,n):
        if n%i==0:
            factors.append(i)
    print('n:',n,'factors:',len(factors))
    return factors


def triangleNumbers(x):
    for i in range(x):
        num = 0
        for j in range(i):
            num+=j
        if i>2 and len(factorsFast(num))>500:
            print("Found!")
            print('ans: ',num)
            print('nth: ',i)
            print(len(factorsFast(num)))
            break
        else:
            continue

if __name__ == '__main__':
    triangleNumbers(200000)

# ans = 76576500
