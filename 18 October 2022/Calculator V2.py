"""Calculator V2"""
def main():
    """Calculator V2"""
    num = int(input())
    tmp = num
    inum = 2
    count = 0
    minus = "9"
    while True:
        if num == 0:
            break
        if tmp == 1:
            count = 1
            break
        if num - int(minus) < 0:
            count += num*inum
            num -= num
        else:
            num -= int(minus)
            count += int(minus)*inum
            inum += 1
            minus += "0"
    print(count)
main()
