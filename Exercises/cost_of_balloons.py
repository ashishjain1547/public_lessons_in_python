T = int(input()) # num of test cases

for i in range(T):
    costs = input().split()
    costs = [int(c) for c in costs]

    min_cost = 0
    max_cost = 0
    if(costs[0] >= costs[1]):
        max_cost = costs[0]
        min_cost = costs[1]
    else:
        max_cost = costs[1]
        min_cost = costs[0]

    n = int(input()) # num of participants

    x_cnt = 0
    y_cnt = 0

    for j in range(n):
        status = input().split()
        if(status[0] == '1'):
            x_cnt += 1
        if(status[1] == '1'):
            y_cnt += 1

    if(x_cnt <= y_cnt):
        print(x_cnt * max_cost + y_cnt * min_cost)
    else:
        print(x_cnt * min_cost + y_cnt * max_cost)