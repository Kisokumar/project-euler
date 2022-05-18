# Multiples of 3 or 5
# Find sum of all multiples of 3 or 5 below 1000

def sol(x):
    ans = 0
    for i in range(x):
        if i%5==0 or i%3==0:
            ans+=i
    print(ans)

sol(1000)

# ans = 233168
