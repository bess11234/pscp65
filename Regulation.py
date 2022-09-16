"""1-15"""
def main():
    """1-15"""
    aaa = int(input())
    bbb = float(input())
    ccc = input()
    space1 = 30
    space2 = 40
    minus = ""
    if aaa < 0:
        minus = str(aaa)[0]
        aaa = str(aaa)[1:]
        space1 -= 1
    length_a = len(str(aaa))
    length_c = len(ccc)
    print(" "*(space1-length_a)+minus+str(aaa))
    print(minus+"0"*(space1-length_a)+str(aaa))
    print("%.2f"%bbb)
    print("%.12f"%bbb)
    print(" "*(space2-length_c)+ccc)
main()
