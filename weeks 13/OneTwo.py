"""OneTwo"""
def main():
    """OneTwo"""
    num, lis = int(input()), []
    for i in range(num):
        if i == 0 or i == 1:
            lis.append(str(i+1))
        else:
            lis.append(lis[i-1]+lis[i-2])
    print(lis[-1])
main()
