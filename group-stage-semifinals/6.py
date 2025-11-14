
# rotational edit distance
# the trick to the problem lies in the words, "...after applying any number of left-rotations"
# this means we can just bruteforce every possible rotations on the string and check the edit distance for each 


# there is another "calculate distance" mechanic we can modularize 

def calc_distance(a, b):
    return sum(1 for i in range(len(a)) if a[i] != b[i])

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
min_edit_distance = calc_distance(s1, s2)

for i in range(len(s1)):
    s1 = s1[1:] + s1[:1]
    dist = calc_distance(s1, s2)

print(f"Minimum edits: {min_edit_distance}")
