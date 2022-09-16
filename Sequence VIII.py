"""Sequence VIII"""
def main(num):
    """Sequence VIII"""
    inum = num
    space = (inum-1)*3
    for i in range(1, num+1):
        for j in range(1, i+1):
            if j == 1:
                print(" "*space+"%02d "%j, end="")
            elif i == j:
                print("%02d"%i, end="")
            else:
                print("%02d "%j, end="")
        space -= 3
        print()
main(int(input()))
