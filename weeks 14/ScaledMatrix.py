"""ScaledMatrix"""
def main():
    """ScaledMatrix"""
    lis, lis2 = [], []
    num, num2 = int(input()), int(input())
    for _ in range(num):
        tmp = []
        for _ in range(num2):
            tmp2 = float(input())
            tmp.append(tmp2)
            lis2.append(tmp2)
        lis.append(tmp)
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            lis[i][j] = "%.2f"%((lis[i][j]-min(lis2))/(max(lis2)-min(lis2)))
    for i in lis:
        print(*i)
main()
