"""MultiplyMatrixPQR"""
def main():
    """MultiplyMatrixPQR"""
    num_p, num_q, num_r = int(input()), int(input()), int(input())
    lis_a = []
    for _ in range(num_p):
        tmp = []
        for _ in range(num_q):
            tmp.append(int(input()))
        lis_a.append(tmp)
    lis_b = []
    for _ in range(num_q):
        tmp = []
        for _ in range(num_r):
            tmp.append(int(input()))
        lis_b.append(tmp)
    lis_c = []
    tmp2 = []
    for i in range(num_r):
        tmp = []
        for j in range(num_q):
            tmp.append(lis_b[j][i])
        tmp2.append(tmp)
    lis_b = tmp2
    for i in range(num_p):
        tmp = []
        for j in range(num_r):
            tmp2 = 0
            for k in range(num_q):
                tmp2 += (lis_a[i][k]*lis_b[j][k])
            tmp.append(tmp2)
        lis_c.append(tmp)
    for i in lis_c:
        print(*i)
main()
