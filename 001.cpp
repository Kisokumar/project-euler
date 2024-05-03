// Problem 1 - Multiples of 3 or 5
// Find sum of all multiples of 3 or 5 below 1000

#include <iostream>

int sol(int num) {
    int ans = 0;
    for (int i = 0; i < num; ++i) {
        if (i % 5 == 0 || i % 3 == 0) {
            ans += i;
        }
    }

    return ans;
}

int main() {
    int outputNumber = sol(1000);
    std::cout << "Solution: " << outputNumber << std::endl;

    return 0;
}

// ans = 233168