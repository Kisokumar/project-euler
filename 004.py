# Problem 4 - Largest palindrome product
# Find largest palindrome number made from the product of two 3-digit numbers

class sol():
    def isPalindrome(x):
        x = str(x)
        num = [c for c in x]
        rev = num[::-1]
        if rev==num:
            return True
        else:
            return False

    def __init__(self):
        nums = [i for i in range(1000,100,-1)]
        ans = 0
        for i in nums:
            for j in nums:
                num = i*j
                if sol.isPalindrome(num):
                    if num>ans:
                        ans=num
        print(ans) 

sol()

# ans = 906609
