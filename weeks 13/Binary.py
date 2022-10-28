"""Binary"""
def main():
    """Binary"""
    num, tmp, count, total = int(input()), 1, 0, 0
    while num != 0:
        if tmp > num:
            tmp -= tmp/2
            num -= tmp
            total += int("1"+"0"*(count-1))
            tmp, count = 1, 0
            continue
        tmp = tmp*2
        count += 1
    print(total)
main()
