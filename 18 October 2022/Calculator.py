"""Calculator"""
def main():
    """Calculator"""
    num = int(input())
    total = 0
    inum = 2
    length = 1
    count = 0
    for i in range(1, num+1):
        if length != len(str(i)):
            length = len(str(i))
            inum += 1
        num -= 1
        count += 1
        total += inum
    if num == 1:
        print(1)
    else:
        print(total)
main()
