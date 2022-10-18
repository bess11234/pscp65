'''diamond'''
def main():
    '''diamond'''
    num = int(input())
    space1 = num//2
    space2 = 1
    for _ in range(num//2):
        if _ == 0:
            print(' '*space1+'*')
            space1 -= 1
        else:
            print(' '*space1+'*'+' '*space2+'*')
            space2 += 2
            space1 -= 1
    print("*"*num)
    space1 = 1
    space2 -= 2
    for _ in range(num//2):
        if _ == num//2-1:
            print(' '*space1+'*')
            space1 += 1
        else:
            print(' '*space1+'*'+' '*space2+'*')
            space2 -= 2
            space1 += 1
main()
