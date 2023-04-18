name = "Johanth Yada" # Variable declaration

# What a string is? A string is a list of characters that we can iterate.

# We iterate over a sequence using the "in" keyword.

# for i in name:
#     print(i)

# USING INTERATION OR FOR-LOOP
cntr = 1 # This is because we need to pick every second character only. To keep a track of our characters in the string.
for i in name:
    if(cntr % 2 == 0):
        print(i)
    cntr += 1


print("----------")
# STRING INDEXING
print(name[1 : len(name) : 2]) # start index (0), end index (length - 1), step (1)
# Stings indexing starts from 0. And the first character we wanted was on index number "1".


names = "Johanth Yada, Shaurya"
print("----------")
# STRING INDEXING
print(names[5 : len(names) : 2]) # start index (0), end index (length - 1), step (1)
# Stings indexing starts from 0. And the first character we wanted was on index number "1".
