"""isPrime_large"""
def main():
    """isPrime_large"""
    check = "YES"
    num = int(input())
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            check = "NO"
            break
    if num == 0 or num == 1:
        check = "NO"
    print(check)
main()
