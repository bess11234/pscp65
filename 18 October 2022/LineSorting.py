"""LineSorting"""
def main():
    """LineSorting"""
    lis = []
    for _ in range(int(input())):
        lis.append(input())
    print(*sorted(lis, key=len), sep="\n")
main()
