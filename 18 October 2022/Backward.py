"""AscendingSort"""
def main():
    """AscendingSort"""
    lis = []
    for _ in range(5):
        num = int(input())
        lis.append(num)
    lis.sort()
    print(*lis, sep="\n")
main()
