"""EuclideanDistance"""
def main():
    """EuclideanDistance"""
    lis, dis = [], 0
    for _ in range(int(input())):
        lis.append(list(map(int, input().split())))
    start, stop = 0, 1
    while stop != len(lis):
        xx1, yy1 = lis[start][0], lis[start][1]
        xx2, yy2 = lis[stop][0], lis[stop][1]
        dis += ((xx2-xx1)**2+(yy2-yy1)**2)**0.5
        start += 1
        stop += 1
    print("%.2f"%dis)
main()
