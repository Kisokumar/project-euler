# Problem 2
# Sum of even fibonacci numbers below 4 million.

def sol(z):
    ans = 0
    x,y = 1,2
    
    while x<z:
        if x%2==0:
            ans+=x
        temp = x+y
        x=y
        y=temp

    return ans

print(sol(4000000))

ans = 4613732
