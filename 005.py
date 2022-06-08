# Problem 5 - Smallest multiple 
# Smallest possible number that is evenly divisible by all of the numbers from 1 to 20

def sol():
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

sol()

# ans = 232792560
