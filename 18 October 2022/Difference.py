"""Difference"""
def main():
    """Difference"""
    aaa, bbb = set(), set()
    num, num2 = int(input()), int(input())
    for _ in range(num):
        nnn = int(input())
        aaa.add(nnn)
    for _ in range(num2):
        nnn = int(input())
        bbb.add(nnn)
    print(*sorted(aaa.difference(bbb)))
main()
