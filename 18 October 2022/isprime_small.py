"""isprime_small"""
def main():
    """isprime_small"""
    check = 0
    num = int(input())
    for i in range(2, num):
        if num%i == 0:
            check = 1
    print("No"*(check == 1 or num == 1)+"Yes"*(check == 0 and num != 1))
main()
