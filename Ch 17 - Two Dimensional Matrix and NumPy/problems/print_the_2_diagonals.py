matrix = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P']]

# Given a two dim. matrix
rows = cols = len(matrix)

print("Diagonal top-left to bottom-right")
for i in range(rows):
    for j in range(cols):
        if(i == j):
            print(matrix[i][j])

print("Diagonal top-right to bottom-left")
for i in range(rows):
    for j in range(cols):
        if(i + j == rows - 1):
            print(matrix[i][j])
