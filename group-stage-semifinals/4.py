

# optimal string rotation
# self explanatory, we only really care about excecution in this problem

# first point to note, there is a "calculate cost score" mechanic that we can convert to a function for simplicity

def calc_score(a):
    # we can use the zip trick below to make a pairing of each adjacent characters in a string
    # for example, if the string was "abc", this would give us [('a', 'b'), ('b', 'c')]
    # as for why this happens, we basically offsetted the string by 1 char to the right
    # so the first character is paired with the second, the second with the third, etc.
    # NOTE: the last char without a pairing is omitted

    # as for computing their score, we know we can utilize ord() in this case to get a numerical representation of the characteres
    # so ord('a') gives us 97, ord('b') gives us 98, etc.
    return sum(abs(ord(c) - ord(d)) for c, d in zip(a, a[1:]))


s = input("Enter the string: ")

min_score = calc_score(s)
for i in range(len(s)):
    s = s[1:] + s[:1] # rotate by 1 char every iteration, NOTE: remember this trick to rotate
    score = calc_score(s)
    min_score = min(min_score, score)
print(f"Minimum score: {min_score}")