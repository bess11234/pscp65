'''One For All'''
def main():
    '''One For All'''
    length = int(input())
    for i in range(length):
        hero = input()
        if i == 0:
            print(hero, end='')
        elif i%2 == 0:
            print('-'*i+hero, end='')
        else:
            print('*'*i+hero, end='')
    if length != 0:
        print('_%d'%length)
main()
