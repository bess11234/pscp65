"""Stamps"""
def main():
    """Stamps"""
    order = int(input())
    goal_money = int(input())
    stamp = int(input())
    every_stamp = int(input())
    discount = int(input())
    had_s = 0
    total = 0
    for _ in range(order):
        cost = int(input())
        had_d = cost
        while True:
            if had_s >= every_stamp and had_d > 0:
                had_s -= every_stamp
                had_d -= discount
            else:
                break
        if cost >= goal_money:
            if goal_money != 0 or discount != 0:
                had_s += (had_d//goal_money)*stamp
        if had_d <= 0:
            total += 0
        else:
            total += had_d
    print("%d"%total)
    print("%d"%had_s)
main()
