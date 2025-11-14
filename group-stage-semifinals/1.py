
# longest plateau
# a plateau is just a sequence of consecutive elements that are the same
# compared to other problems where a plateau must have strictly increasing elements, this problem doesnt really care about that
# whenever a problem is about manipulating consecutive adjancent elements in a list, itertools.groupby

from itertools import groupby 

# this is a good method of getting a sequence of elements, knowing how to do this will save you time
d = list(map(int, input("Enter a sequence (-1 to end): ").split()[:-1])) # take note here, i removed the -1 as WOULD cause issues later
p = max([len(list(g)) for _, g in groupby(d)] + [0]) # tldr, groupby returns a tuple of the element and a "generator". so we need to unpack it to get the generator using list() then get its length
print(f"Longest Plateau: {p}")



