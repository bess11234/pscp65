"""Amicable"""
def check(num):
    """Amicable"""
    total = 1
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            total += i+num//i
    return total
def main():
    """Amicable"""
    num, total, inum, lis = int(input()), 0, 220, []
    while inum <= num:
        tmp = check(inum)
        if check(tmp) == inum and inum != tmp and inum not in lis:
            lis.append(tmp)
            total += tmp+inum
        inum += 1
    print(total)
main()
