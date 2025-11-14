

# alternating parity snake

n, m = list(map(int, input("Enter the number of rows and columns: ").split()))
print("Enter the matrix elements: ")
d = [list(map(int, input().split())) for _ in range(n)]

# try to divide and conquer your problems
# for example, there is the problem of alternating parities in a matrix
# then there is also the problem of snake traversal in a matrix
# trick is to split them

# get snake traversal
d = []
for i in range(n): 
    start,end, increment  = (0, m, 1) if i % 2 == 0 else (m - 1, -1, -1)
    for j in range(start, end, increment):
        d.append(d[i][j])

# get alternating parities
# there are multiple approaches to this, i used the most intuitive one 

# we start with a beginning parity
# this starting parity flips per element
# if the current element we currently have does not match this parity, we increment score (meaning that element has to be modified)
# NOTE: modifying an element (adding 1) is sure to flip the parity just saying
# we have 2 cases of this beginning parity so we can turn this to a function


def solve(par): # starting parity
    res = 0
    for e in d:
        if e != par:
            res += 1
        par ^= 1 # flips here
    return res

res = min(solve(0), solve(1)) # solve for both cases
print(f"Minimum modifications: {res}")
