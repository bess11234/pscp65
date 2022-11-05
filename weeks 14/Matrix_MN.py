"""Matrix_MN"""
def main():
    """Matrix_MN"""
    lis = []
    num, num2 = int(input()), int(input())
    for _ in range(num):
        tmp = []
        for _ in range(num2):
            tmp.append(int(input()))
        lis.append(tmp)
    for i in lis:
        print(*i)
main()
