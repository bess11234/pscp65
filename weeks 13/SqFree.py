"""SqFree"""
def squafree(num):
    """squafree"""
    if num%2 == 0:
        num = num/2
    if num%2 == 0:
        return False
    for i in range(3, int(num**0.5)+1):
        if num%i == 0:
            num = num/i
        if num%i == 0:
            return False
    return True
def main():
    """SqFree"""
    count = 0
    for i in range(1, int(input())+1):
        if squafree(i):
            count += 1
    print(count)
main()
