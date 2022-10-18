"""pscp"""
def main():
    """pscp"""
    cost = int(input())
    amount = int(input())
    free = int(input())
    least = int(input())
    total = 0
    donut = 0
    stack = least//(amount+free)
    total += (cost*amount)*stack
    donut += (amount+free)*stack
    least -= (amount+free)*stack
    if least < amount:
        total += least*cost
        donut += least
    else:
        total += cost*amount
        donut += amount+free
    print("%d %d"%(total, donut))
main()
