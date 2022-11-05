"""PairNumbering"""
def main():
    """PairNumbering"""
    import json
    lis_a = json.loads(input())
    lis_b = json.loads(input())
    goal = int(input())
    count = 0
    tmp = []
    lis_a = list(filter(lambda num: num <= goal, lis_a))
    lis_b = list(filter(lambda num: num <= goal, lis_b))
    for i in lis_b:
        if i not in tmp:
            tmp.append(i)
    for i in lis_a:
        for j in tmp:
            if i+j == goal:
                count += lis_b.count(j)
    print(count)
main()
