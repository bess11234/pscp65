'''[Recommend] Squid Game 3 - Tug-of-War'''
def main():
    '''[Recommend] Squid Game 3 - Tug-of-War'''
    power_a = 0
    power_b = 0
    for _ in range(10):
        power = int(input())
        power_a += power
    for _ in range(10):
        power = int(input())
        power_b += power
    if power_a > power_b:
        print("B")
    elif power_a < power_b:
        print("A")
    else:
        print("AB")
main()
