# Problem 6 - Sum square difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def sol(x):
    sumSquares,squareSum = 0,0
    for i in range(x+1):
        sumSquares+=(i**2)
        squareSum+=i
    squareSum**=2

    return (squareSum-sumSquares)

print(sol(100))

# ans = 25164150
