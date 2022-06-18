# Problem 10 - Summation of primes
# Find the sum of all primes below two million

from math import isqrt

class sol:
    def __init__(self):
        print(sol.sieveSum(2000000))

    def sieveSum(n):
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

        return sum([i for i in range(n) if isPrime[i]])

if __name__ == '__main__':
    sol()

# ans = 142913828922
