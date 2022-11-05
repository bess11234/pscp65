"""isPrime_large"""
def main():
    """isPrime_large"""
    check = True
    num = int(input())
    for i in range(2, int(num**0.5)+1, 3):
        if num%i == 0:
            check = False
            break
    if num == 0 or num == 1:
        check = False
    print(check)
main()
