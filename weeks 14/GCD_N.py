"""GCD_N"""
def main():
    """GCD_N"""
    lis = []
    for _ in range(int(input())):
        lis.append(int(input()))
    lis.sort()
    while True:
        if len(lis) == 1:
            break
        while min(lis[0], lis[1]):
            lis[0], lis[1] = min(lis[0], lis[1]), max(lis[0], lis[1])%min(lis[0], lis[1])
        lis.append(max(lis[0], lis[1]))
        del lis[0]
        del lis[0]
        lis.sort()
    print(lis[0])
main()
