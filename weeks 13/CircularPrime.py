"""CircularPrime"""
def isprime(num):
    """isPrime_large"""
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return None
    return num
def main():
    """CircularPrime"""
    lis, lis2 = [], []
    for i in range(2, int(input())+1):
        if isprime(i) != None:
            lis.append(i)
    for i in lis:
        tmp = str(i)
        for j in range(len(str(i))):
            if len(str(i)) == 1:
                lis2.append(i)
            else:
                tmp = tmp[1:]+tmp[0]
                if isprime(int(tmp)) == None:
                    break
                elif j == len(str(i))-1:
                    lis2.append(i)
    print(sum(lis2))
main()
