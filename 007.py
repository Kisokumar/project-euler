# Problem 7 - 10001st prime
# What is the 10001st prime number?

from math import isqrt

class sol:
    def __init__(self,n):
        sol.findPrimeFast(n)

    def sieve(n):
        """Implementation of the Sieve of Eratosthenes algorithm"""
        if n<=2:
            return []
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        for i in range(2, isqrt(n)):
            if isPrime[i]:
                for x in range(i*i, n, i):  # Reducing runtime by beginning at square of i.
                    isPrime[x] = False
        return [i for i in range(n) if isPrime[i]]

    def findPrimeSlow(n):
        """"Uses the sieve function to iteratively find Nth prime."""
        c = 10000
        print('Running. . .')
        while 1:
            temp = len(sol.sieve(c))
            if temp==n:
                print(sol.sieve(c)[-1])
                break
            else:
                c+=1

    def findPrimeFast(n):
        """Finds all primes in large range using sieve function and checks if given index is within the range."""
        found = False
        c = 100
        while not found:
            if len(sol.sieve(c))<n:
                c*=10
            else:
                print(sol.sieve(c)[n-1])
                found = True    

if __name__ == '__main__':
    sol(10001)

# ans = 104743
