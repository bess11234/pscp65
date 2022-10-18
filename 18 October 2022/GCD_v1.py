"""GCD_v1"""
def main():
    """GCD_v1"""
    num, num2, tmp = int(input()), int(input()), 0
    lis1, lis2, lis3 = [], [], []
    for i in range(1, num+1):
        if num//i == num/i:
            lis1.append(i)
    for i in range(1, num2+1):
        if num2//i == num2/i:
            lis2.append(i)
    for i in lis1:
        if i in lis2:
            lis3.append(i)
    if lis3 == []:
        tmp = num*(num2 == 0)+num2*(num == 0)
        lis3.append(tmp)
    lis3 = lis3[::-1]
    print(lis3[0])
main()
