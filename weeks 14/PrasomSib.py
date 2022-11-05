"""PrasomSib"""
def main():
    """PrasomSib"""
    text = input()
    count = 0
    start, stop, plus = 0, 2, 0
    while True:
        if len(text) < stop+plus:
            break
        tmp = text[start:stop+plus]
        lis = list(map(int, list(tmp)))
        if sum(lis) == 10:
            count += 1
            start += 1
            stop += 1
        if sum(lis) < 10:
            plus += 1
        if sum(lis) > 10:
            start += 1
            stop += 1
            plus = 0
    print(count)
main()
