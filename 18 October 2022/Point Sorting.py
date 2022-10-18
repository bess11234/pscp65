"""Point Sorting"""
def main():
    """Point Sorting"""
    lis = []
    total = 0
    for _ in range(int(input())):
        for _ in range(int(input())):
            vec = input().split()
            vec = list(map(int, vec))
            total = sum(vec)
            tmp = [total]
            tmp.extend(vec)
            lis.append(tmp)
        lis.sort()
        for i in range(len(lis)):
            print(lis[i][1], lis[i][2])
        lis = []
main()
