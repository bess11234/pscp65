'''Saitama'''
def main():
    '''Saitama'''
    goal_a = int(input())
    goal_b = int(input())
    goal_c = int(input())
    goal_d = int(input())
    able_a = int(input())
    able_b = int(input())
    able_d = int(input())
    able_c = int(input())
    least_a = day(goal_a, able_a)
    least_b = day(goal_b, able_b)
    least_c = day(goal_c, able_c)
    least_d = day(goal_d, able_d)
    atleast = most(least_a, least_b)
    atleast = most(atleast, least_c)
    atleast = most(atleast, least_d)
    print(atleast)
def day(goal, able):
    """day"""
    total = 0
    while goal > 0:
        goal -= able
        total += 1
    return total
def most(val, val2):
    """most"""
    if val >= val2:
        return val
    else:
        return val2
main()
