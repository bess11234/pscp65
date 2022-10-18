"""Classify"""
def main():
    """Classify"""
    lis = []
    while True:
        std = input()
        if std == "END":
            break
        tmp2 = ""
        tmp = [int(std[:2]), [int(std[2:4])]]
        for i in range(len(lis)):
            if lis[i].count(int(std[:2])) == 1:
                lis[i][1].append(int(std[2:4]))
                tmp2 = i
                break
        if isinstance(tmp2, int):
            lis[tmp2][1].sort()
        else:
            lis.append(tmp)
    lis.sort()
    count = 1
    tmp = 1
    tmp2 = ""
    check = 0
    for i in range(len(lis)):
        tmp2 = lis[i][1][0]
        while tmp != len(lis[i][1]):
            if tmp2 == lis[i][1][tmp]:
                count += 1
            else:
                print(str(lis[i][0])*(check == 0)+"--"*(check == 1), tmp2, count)
                tmp2 = lis[i][1][tmp]
                count = 1
                check = 1
            tmp += 1
        print(str(lis[i][0])*(check == 0)+"--"*(check == 1), tmp2, count)
        tmp = 1
        count = 1
        check = 0
main()
