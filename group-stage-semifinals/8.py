# matrix zero transformation

# i like this problem, its on leetcode i think
# this problem requires a great deal of thinking, especially on the concept of flipping or xoring
# so i will explain it here

# FIRST POINT:
# when we flip a row or a column, it's unreasonable to flip it again 
# this is because flipping a row or a column twice is the same as not flipping it at all

# SECOND POINT: 
# we want ALL elements to be zero right? 
# this means its reasonable to begin our thought process with the first row 

# example 1:
# [1, 0, 1]
# [0, 1, 1] 
# [1, 1, 0]

# we can see the first row is 1, 0, 1
# our goal is to make all elements 0
# flipping the row itself doesn't really solve our problem since this would also flip the rows 0's to 1's
# therefore, we have to somehow flip columns
# in our case, the columns in need of flipping are columns that have 1's (0th and 2nd column)
# so we flip the columns 0 and 2, cool, so now the first row contain all 0's 

# new matrix: 
# [0, 0, 0]
# [1, 1, 0] 
# [0, 1, 1]

# we aren't done however as we still have to check whether all the other rows
# we can't flip the ANY column EVER again. why? this is because flipping any of the columns would also "break" the first row which already contains all 0's
# this means, we can only either flip or not flip the succeeding rows
# the idea is we are hoping that the next rows all have either all 1's (in which case we flip the row) or all 0's (in which case we don't flip the row)

# HOWEVER, we aren't done yet again
# we have one more option. why not, flip the first row? 
# we know flipping the first row would flip the 0's to 1's and the 1's to 0's (meaning it wouldn't solve it)
# however, what if that arrangement of 0's and 1's and in turn, that arrangement of column flips is better?



n, m = list(map(int, input("Enter the row and col: ").split()))
print("Enter the grid: ")
d = [list(map(int, input().split())) for _ in range(n)]

def solve(d):
    col = set()
    for j in range(m):
        if d[0][j]:
            col.add(j)
    res = len(col)
    for i in range(1, n):
        q = sum(d[i][j] ^ (j in col) for j in range(m))
        if q != m or q != 0:
            return int(1e9)
        res += q == m
    return res

res = solve(d)

for j in range(m):
    d[0][j] ^= 1

res = min(res, solve(d) + 1)

print(f"Result: {res if res != int(1e9) else -1}")