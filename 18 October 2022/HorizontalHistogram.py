"""HorizontalHistogram"""
def main():
    """HorizontalHistogram"""
    txt = list(input())
    lis = []
    tmp = []
    for i in sorted(txt, key=str.lower):
        if i == i.lower() and i not in lis:
            lis.append(i)
        elif i == i.upper() and i not in tmp:
            tmp.append(i)
    lis.extend(tmp)
    for i in lis:
        print(i, end=" : ")
        for j in range(txt.count(i)):
            if j%5 == 0 and j != 0:
                print("|-", end="")
                continue
            print("-", end="")
        print()
main()
