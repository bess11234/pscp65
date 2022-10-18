'''Shorten'''
def main():
    '''Shorten'''
    before = ""
    fst = 0
    check = 0
    while True:
        num = int(input())
        if before == "":
            fst = num
            before = str(num)
        elif num-int(before) == 1:
            before = str(num)
        else:
            print(", "*(check == 1), fst, "-"*(before != str(fst)),\
                  before*(before != str(fst)), sep="", end="")
            check = 1
            fst = num
            before = str(num)
        if num == -1:
            break
main()
