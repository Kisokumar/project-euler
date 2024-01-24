# Problem 5 - Smallest multiple 
# Smallest possible number that is evenly divisible by all of the numbers from 1 to 20
import numpy as np

def brute():
    nums = [i for i in range(1,21)]
    ans = 1
    found = False
    while found==False:
        ans+=1
        correct = True
        for i in nums:
            temp = ans%i
            if temp!=0:
                correct = False
        if correct:
            found=True
            print(ans)

def sol():
    nums = range(1, 21)
    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = np.lcm(lcm, nums[i])
    print(lcm)

sol()

# ans = 232792560
