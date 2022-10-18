"""Sequence XI"""
def main(num):
    """Sequence XI"""
    inum = num
    count1 = 1
    for i in range(1, num+1):
        for j in range(1, i+1):
            if j == 1:
                print("%02d "%j, end="")
            elif i == j:
                print("%02d "%i, end="")
            else:
                print("%02d "%j, end="")
        inum -= 1
        for k in range(1, num+1):
            if i == k:
                print("%02d "%k*inum, end="")
        for col in range(count1, num):
            if i == col:
                print("%02d "%col, end="")
            else:
                print("%02d "%i, end="")
        for col2 in range(count1-1, 0, -1):
            print("%02d "%col2, end="")
        count1 += 1
        print()
    half(num)
def half(num):
    """half-bottom"""
    inum = 2
    count1 = num-1
    count2 = 1
    for i in range(num, 1, -1):
        for j in range(1, i):
            if j == i-1:
                print("%02d "%j*inum, end="")
            else:
                print("%02d "%j, end="")
        inum += 1
        for k in range(count1, 0, -1):
            if k == count1:
                print("%02d "%k*count2, end="")
            else:
                print("%02d "%k, end="")
        count1 -= 1
        count2 += 1
        print()
main(int(input()))
