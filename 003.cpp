// Problem 3 - Largest Prime Factor
// Largest prime factor of 600851475143

#include <iostream>

int sol(long num) {
    int i = 2;
    while (i * i < num) {
        while (num % i == 0) {
            num = num / i;
        }
        i = i + 1;
    }
    return num;
}

int main() {
    int outputNumber = sol(600851475143);
    std::cout << "Solution: " << outputNumber << std::endl;

    return 0;
}

// ans = 6857