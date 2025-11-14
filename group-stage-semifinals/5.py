

# compact string encoder 
# a bit complicated, but with a bit of thinking its doable

# my approach to this problem is this
# the letters part is techinically just run-length encoding
# this could be done easily with itertools.groupby (again)

# the numbers part is a bit more complicated since we want to pair numbers together
# basically, if if we used itertools groupby, it would be like numbers we're treated as the same

# so why not do that?

# we use groupby

# CASE 1
# if we encounter a letter, we treat it like normal run-length encoding

# CASE: 2
# if we encounter a number, we add it to a temporary string
# this temporary string will be used to pair numbers together
# if we encounter a letter again (or we reach the end), we add the temporary string to the result


from itertools import groupby


s = input("Enter string: ")

res = ""
nums = ""

for c, g in groupby(s):
    l = len(list(g))
    if c.isalpha():
        if nums:
            res += f"[{nums}]"
            nums = ""

        res += c + str(l)
    else:
        nums += c * l
    
if nums:
    res += f"[{nums}]"

print(f"Result: {res}")
    

