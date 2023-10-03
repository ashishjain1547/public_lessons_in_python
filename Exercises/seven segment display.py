d = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

def get_sticks_count(num):
    num = str(num)
    s = 0
    for i in num:
        s += d[i]

    return s

T = int(input())

for i in range(T):
    n = int(input())
    s = get_sticks_count(n)
    if s % 2 == 0:
        num_of_ones = s // 2
        o = '1' * num_of_ones
        print(o)
    else:
        num_of_ones = s // 2
        o = '1' * num_of_ones
        o = o.replace('1', '7', 1)
        print(o)
