'''PhoneNumber'''
def main():
    '''PhoneNumber'''
    num = input()
    nation = input()
    if nation == 'Domestic':
        if len(num) == 9:
            print(num[0]+' '+num[1:5]+' '+num[5:])
        elif len(num) == 10:
            print(num[0:2]+' '+num[2:6]+' '+num[6:])
    else:
        if len(num) == 9:
            print('+66'+' '+num[1:5]+' '+num[5:])
        elif len(num) == 10:
            print('+66'+num[1]+' '+num[2:6]+' '+num[6:])
main()
