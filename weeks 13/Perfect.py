"""Perfect"""
def main():
    """Perfect"""
    num = int(input())
    inum = 1
    total, check = 0, 0
    while inum <= num:
        total2 = 0
        inum2 = inum
        while True:
            total2 += 1/inum2
            inum2 = inum2/2
            if isinstance(inum2%2, float) == True and inum2 != (inum2*2)//2 and not inum2 == 1:
                inum2 = int(inum2)+1
            elif inum2 == 1:
                total2 += 1/inum2
            if inum2 <= 1 and total2 == 2 and check == 1:
                total += inum
                inum = inum*16
                break
            elif inum2 <= 1 and total2 == 2:
                total += inum
                check = 1
                break
            elif inum2 <= 1 and total2 != 2:
                break
        inum += 1
    print(total)
main()
