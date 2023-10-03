import re

with open("Sample_input.txt", mode = 'r') as f:
    data = f.readlines()



no_of_input = data[0]

input_idx = []

# Processing the input
# Producing indices of where tables are located in the input data.
# [[2, 4], [5, 12], [13, 31], ...] This is what will be produced
# i would contain [2, 4], then [5, 12], then [13, 31], so on and so forth

for i in range(len(data)):
    if i == 0:
        # At the line 0: we are having the number representing count of input. We have to skip the first line only.
        continue 

    if re.match(r'^[0-9]', data[i]): 
        # If my line starts with a digit
        # ^ 	Starts with
        # [0-9] Returns a match for any digit between 0 and 9

        idx = []

        idx.append(i + 1)

        num_rows = data[i].split()[0]
        # Range is coming in the form of: num_rows num_cols
        # So we spliting on whitespace and extracting the zeroth element

        idx.append(i + 1 + int(num_rows))
        # i + 1: represents the start. So what would be our end: start + num_rows

        input_idx.append(idx)

# ~~~ Processing input ~~~ ends here

for i in input_idx:
    # [[2, 4], [5, 12], [13, 31], ...] This is what is coming as input_idx
    # i would contain [2, 4], then [5, 12], then [13, 31], so on and so forth

    pattern = data[i[0] : i[1]]

    num_hashes = []
    for j in pattern:
        num_hashes.append(j.count('#'))
    
    print(max(num_hashes))