'''[Recommend] Books'''
def main():
    '''[Recommend] Books'''
    from math import ceil
    book = int(input())
    page = int(input())
    xxx = int(input())
    yyy = int(input())
    day = 0
    total = 0
    while True:
        if book == 0:
            break
        read = ceil(page*xxx/yyy)
        if read >= page:
            break
        total += read
        if total >= page:
            total = 0
            book -= 1
        xxx += 1
        yyy += 1
        day += 1
    print(book+day)
main()
