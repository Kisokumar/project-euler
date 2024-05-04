// Problem 2
// Sum of even fibonacci numbers below 4 million.

#include <iostream>

int sol(int limit) {
    int sum = 0;
    int prev = 1, current = 2;

    while (current < limit) {
        if (current % 2 == 0) {
            sum += current;
        }
        int next = prev + current;
        prev = current;
        current = next;
    }

    return sum;
}

int main() {
    int outputNumber = sol(4000000);
    std::cout << "Solution: " << outputNumber << std::endl;

    return 0;
}

// ans = 4613732