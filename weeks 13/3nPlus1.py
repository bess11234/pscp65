"""3nPlus1"""
def main():
    """3nPlus1"""
    while True:
        num, count = int(input()), 1
        if num == 0:
            break
        while num != 1:
            if num%2 == 0:
                num = num/2
            elif num%2 == 1:
                num = num*3+1
            count += 1
        print(count)
main()
