"""Divide3Or5"""
def main():
    """Divide3Or5"""
    num, total = int(input()), 0
    for i in range(1, num+1):
        if i%3 == 0 or i%5 == 0:
            total += i
    print(total)
main()
