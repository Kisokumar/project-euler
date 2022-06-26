# Problem 16 - Power digit sum
# What is the sum of the digits of the number 2^1000?

def sol():
    powerDigit = 2**1000
    powerDigitStr = str(powerDigit)
    ans = 0
    for c in powerDigitStr:
        ans+=int(c)
    return ans

if __name__ == '__main__':
    print(sol())

# ans = 1366
