# Problem 17 - Number letter counts
# If all the numbers from 1 to 1000 are written out in words

singles = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4 }                # one,two,three...
unique = {11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8 }        # eleven,twelve,thirteen...
tens = {1:3,2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}                     # twenty,thirty,forty...

class countLetters:
    def __init__(self):
        ans = 0
        for i in range(1,1001):
            ans += int((countLetters.count(i)))
        print(ans == 21124)

    def singleDigits(n):
        if n == 0:
            ans = 0
        else:
            ans = singles[n]
        return ans

    def doubleDigits(n):
        ans = 0
        if n in unique:                                 # Handles teen numbers
            ans = unique[n]
        else:
            digits = [digit for digit in str(n)]
            if digits[1] == 0:
                ans = tens[digits[0]]
            else:
                ans = tens[int(digits[0])] + countLetters.singleDigits(int(digits[1]))
        return ans

    def tripleDigits(n):
        digits = [digit for digit in str(n)]
        if n == 1000:
            ans = 11
        elif digits [1] == '0' and digits [2] == '0':   # Handles 200,300...
            ans = countLetters.singleDigits(int(digits[0]))+7
        else:
            ans = 10                                    # Start w/ 10 because numbers 100+ have '___ hundred and ___'=3
            num = [c for c in str(n)]
            ans += singles[int(num[0])]
            if num[1] == '0':                           # If middle digit is 0, we can omit.
                lastDigit = int("".join(num[2]))
                ans+=countLetters.singleDigits(lastDigit)
            else:
                lastTwoDigits = int("".join(num[1:]))   # Split three digits into last two digits and uses double function.
                ans+=countLetters.doubleDigits(lastTwoDigits)
        return ans

    def count(n):
        if n<10:
            ans = countLetters.singleDigits(n)
        elif n<100:
            ans = countLetters.doubleDigits(n)
        elif n>=100:
            ans = countLetters.tripleDigits(n)
        return ans

if __name__ == '__main__':
    countLetters()

# ans = 21124
