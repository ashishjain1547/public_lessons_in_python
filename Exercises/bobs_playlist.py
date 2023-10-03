from collections import Counter

N = int(input())
l = [int(i) for i in input().split()]

most_common = Counter(l).most_common()

favorite_count = most_common[0][1]

m = [i for i in most_common if i[1] == favorite_count]

print(len(m))