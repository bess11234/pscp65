"""Ink"""
def main():
    """Ink"""
    import math
    tmp = list(map(int, input().split()))
    grow, people = tmp[0], tmp[1]
    for _ in range(people):
        tmp, area = list(map(int, input().split())), 0
        area = tmp[0]**2+tmp[1]**2
        area = 3.1416*area
        print(math.ceil(area/grow))
main()
