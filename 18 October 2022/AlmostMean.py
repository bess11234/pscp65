"""AlmostMean"""
def main():
    """AlmostMean"""
    num = int(input())
    lis = []
    for i in range(num):
        lis.append(input().split())
    aver = 0
    for i in range(len(lis)):
        aver += float(lis[i][1])
    gap = 0
    stu = ""
    aver = aver/num
    for i in range(len(lis)):
        if float(lis[i][1]) <= aver:
            if gap == 0:
                stu = lis[i]
                gap = aver-float(lis[i][1])
            elif aver-float(lis[i][1]) <= gap:
                stu = lis[i]
                gap = aver-float(lis[i][1])
    print(*stu, sep="\t")
main()
