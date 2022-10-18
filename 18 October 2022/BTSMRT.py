'''BTSMRT'''
def main():
    '''BTSMRT'''
    day = input()
    age = float(input())
    height = float(input())
    if (age < 14 and height < 90) or (age < 14 and height <= 140 and day == 'Children Day')\
       or (age >= 60 and day == 'Senior Day'):
        print('FREE')
    else:
        print('PAY')
main()
