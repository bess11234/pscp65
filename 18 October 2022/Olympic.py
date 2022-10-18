"""Olympic"""
def main():
    """Olympic"""
    num, count = int(input()), 1
    lis = []
    for _ in range(num):
        txt = input().split()
        tmp = [int(txt[1]), int(txt[2]), int(txt[3]), txt[0],\
               int(txt[1])+int(txt[2])+int(txt[3])]
        lis.append(tmp)
    lis.sort()
    lis = lis[::-1]
    tmp = lis[0][:3]
    fixed = 1
    lis2 = []
    for i in lis:
        if tmp == i[:3]:
            lis2.append([fixed, i[3], i[0], i[1], i[2], i[4]])
        else:
            tmp = i[:3]
            fixed = count
            lis2.append([count, i[3], i[0], i[1], i[2], i[4]])
        count += 1
    for i in sorted(lis2):
        print(*i)
main()
