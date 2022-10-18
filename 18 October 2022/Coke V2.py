"""Coke V2"""
def main():
    """Coke V2"""
    price = int(input())
    goal = int(input())
    pro = int(input())
    least = int(input())
    cost = 0
    if goal != 0 and least > goal:
        least -= goal+1
        cost += (price*goal)+pro
        tmp = least//goal
        least -= tmp
        cost += tmp*pro
    cost += least*price
    print(cost)
main()
