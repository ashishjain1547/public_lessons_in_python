import string 

print(string.ascii_lowercase)

#s = "A quick brown fox jumps over the lazy dog."
s = "A quick brown fox is there."

s = s.lower()

l = [] # ordered, indexed and can contain duplicate elements
b = set() # unordered, unindexed and does not contain duplicate elements

for i in string.ascii_lowercase:
    if i in s:
        print(i,"found")
        b.add("found")
        l.append("found")
    else:
        print(i,"not found")
        b.add("not found")
        l.append("not found")
 
print(l)
print(b)

if 'found' in b and len(b) == 1:
    print("Pangram Found")
else: 
    print("String is not a pangram")


# List is ordered. Set is unordered.
# print(list(s))
# print(set(s))