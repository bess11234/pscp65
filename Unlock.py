'''[Recommend] Diginity'''
def main():
    '''[Recommend] Diginity'''
    while True:
        num = int(input())
        if num == 0:
            break
        length = len(str(num))
        while length != 1:
            num = unlock(num)
            length = len(str(num))
        print(num)
def unlock(num):
    """UNLOCK"""
    total = 0
    for i in str(num):
        total += int(i)
    return total
main()
