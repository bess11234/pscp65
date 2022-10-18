"""Duplicate I"""
def main():
    """Duplicate I"""
    aaa, bbb, dup = [], [], []
    num, num2 = int(input()), int(input())
    for _ in range(num):
        nnn = int(input())
        aaa.append(nnn)
    for _ in range(num2):
        nnn = int(input())
        bbb.append(nnn)
    if len(aaa) <= len(bbb):
        group = aaa
        diff = bbb
    else:
        group = bbb
        diff = aaa
    for i in range(len(group)):
        if diff.count(group[i]) > 0:
            dup.append(group[i])
    if dup != []:
        print(*sorted(dup, reverse=True), sep="\n", end="")
    else:
        print("Nope")
main()
