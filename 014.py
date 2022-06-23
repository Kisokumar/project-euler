# Problem 14 - Longest Collatz sequence
# Return the number under 1 million which produces the longest Collatz sequence

def isEven(n):
    return n%2==0
       
def collatzSequence(n):
    ans = [n]
    while ans[-1]!=1:
        last = ans[-1]
        if isEven(int(last)):
            ans.append(last//2)
        else:
            ans.append((3*last)+1)

    return len(ans)

def sol():
    lengths = {}
    for i in range(2,1000000):
        lengths[collatzSequence(i)]=i
    
    return lengths[max(lengths)]

if __name__ == '__main__':
   print(sol())

# ans = 837799
