"""All_Primes"""
def main():
    """All_Primes"""
    count = 0
    check = 0
    num = int(input())
    if num > 1:
        for i in range(2, num+1):
            for j in range(2, i):
                if i%j == 0:
                    check = 1
            count += 1*(check == 0)
            check = 0
    print(count)
main()
