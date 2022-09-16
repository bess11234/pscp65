"""pscp"""
def main():
    """pscp"""
    s_brick = int(input())
    l_brick = int(input())
    goal = int(input())
    limit_l = goal//5
    if limit_l >= l_brick:
        goal -= 5*l_brick
    if limit_l < l_brick:
        goal = goal%5
    if goal == 0:
        print("0")
    else:
        if s_brick >= goal:
            print(goal)
        elif goal != 0:
            print("-1")
main()
