N = int(input())

# A = list(map(int, input().split()))

A = input()

# A = "25 6 71 43"
# If you split is: ["25", "6", "71", "43"]
# 3 of 43 of A: that would be A[-1][-1]

last_digit = A[-1]

if last_digit == '0':
    print('Yes')
else:
    print('No')