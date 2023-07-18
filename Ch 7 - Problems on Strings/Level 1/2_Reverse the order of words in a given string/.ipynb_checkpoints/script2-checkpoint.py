# python code to reverse words in a given string
 
# input string
string = "i like this program very much"
 
# spliting words in the given string
# using slicing reverse the words
s = string.split()[::-1]
 
# joining the reversed string and
# printing the output
print(" ".join(s))