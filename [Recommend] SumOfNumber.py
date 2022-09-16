"""pscp"""
def main(limit):
    """pscp"""
    total = 0
    while True:
        num = int(input())
        if num < 0:
            break
        total += num
        if total == limit:
            break
    print(total)
main(int(input()))
