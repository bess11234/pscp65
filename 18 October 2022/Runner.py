"""Runner"""
def main():
    """Runner"""
    dis = int(input())
    tmp = []
    lis = []
    for i in range(1, int(input())+1):
        runner = input().split()
        tmp = [(dis-int(runner[1]))/int(runner[0]), int(runner[0]), i]
        lis.append(tmp)
    lis.sort()
    while len(lis) > 1:
        if lis[1].count(lis[0][0]) == 1:
            if lis[1][1] > lis[0][1]:
                del lis[0]
            else:
                del lis[1]
        else:
            break
    print(lis[0][2])
main()
