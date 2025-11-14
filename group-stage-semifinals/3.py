
# bitwise AND chain
# in this problem, we are building a chain of elements, kinda like doing a running sum

# in this chain, we only really care about adjacent elements

# for example, in the given example [3, 6, 12, 5, 10]
# 3 AND 6 > 0, therefore, 6 can be part of the chain that begins at 3
# so next, we check is 6 AND 12 > 0? it does so we move on to the next element

# this goes on until we reach an element that doesnt "fit", if it doesnt fit, then we form a new chain
# this new chain will start with the element that doesnt fit, in the example, that would be 5



n = int(input("Enter array size: "))
d = list(map(int, input("Enter the array elements: \n").split()))

res = 0
curr =  1 # we begin at 1 since we want to include the first element in the chain
for i in range(1, n): 
    if (d[i] & d[i - 1]) > 0: # NOTE: be careful on bitwise operations order of operations, i forgot if AND takes precedence over > but better be safe than sorry :p
        curr += 1 
    else:
        curr = 1 # we set to 1 since we want to include the element that no longer fits in the current chain
    res = max(res, curr)
print(f"Longest AND chain: {res}")


