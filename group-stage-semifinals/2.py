

# string rotation checker
# in most codechum problems, its important to consider time to write and time complexity
# in this case, length of 100 is too little to care about time complexity
# so we rush it, a simple list compre + all will do the trick

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

r = any(s2 == s1[i:] + s1[:i] for i in range(len(s1)))
print(f"Rotation: {'Yes' if r else 'No'}")