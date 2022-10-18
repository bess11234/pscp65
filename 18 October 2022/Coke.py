"""Coke"""
def main():
    """Coke"""
    price = int(input())
    goal = int(input())
    pro = int(input())
    least = int(input())
    cost = 0
    coke = 0
    cap = 0
    while coke < least:
        if cap == goal and goal != 0:
            cost += pro
            cap = 1
        else:
            cost += price
            cap += 1
        coke += 1
    print(cost)
main()
