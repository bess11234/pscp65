"""[Recommend] Milk"""
def main():
    """[Recommend] Milk"""
    price = int(input())
    cap = int(input())
    free = int(input())
    money = int(input())
    total_cap = money//price
    total_free = 0
    left = 0
    if cap != 0 and total_cap >= cap:
        while True:
            total_cap -= cap
            if total_cap < 0:
                break
            total_cap += free
            total_free += 1
            left = total_cap
        result_milk = total_free*cap+left
        print(result_milk)
    else:
        print(total_cap)
main()
