'''Century'''
def main():
    '''Century'''
    num = int(input())
    for _ in range(num):
        year = input()
        type1 = year[:4].upper()
        year = year[5:]
        if not type1 in "A.D. B.E." or year.isdecimal() == False:
            print("ERROR")
            continue
        if type1 == "B.E.":
            year = str(int(year)-543)
            if int(year) < 0:
                print("ERROR")
                continue
        if int(year[-2:]) > 0:
            century = int(year)//100+1
            print(century)
        else:
            century = int(year)//100
            print(century)
main()
