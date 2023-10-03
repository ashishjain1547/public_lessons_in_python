N = int(input("Enter length:"))
A = [int(i) for i in input("Enter the array:").split()]


def get_special_sum(A, index):
    flag = True 
    i = 1
    s = 0
    while flag:
        ix_last = index + i 
        
        if (ix_last < len(A)):
            s += sum(A[index : ix_last])
        else:
            flag = False 

        # Updates
        i += 1
        index = ix_last + 1

index = int(input("Enter the index:"))
print(get_special_sum(A, index))