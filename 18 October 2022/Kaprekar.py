"""Kaprekar"""
def main():
    """Kaprekar"""
    num = "%04d"%int(input())
    if len(num) < 4:
        num += "0"
    fst, sec, trd, four = more1(num[0], num[1], num[2], num[3])
    inum = 0
    while True:
        highest = int(fst+sec+trd+four)
        lowest = int(str(highest)[::-1])
        result = highest-lowest
        inum += 1
        result = str(result)
        if len(result) < 4:
            result += "0"
        fst, sec, trd, four = more1(result[0], result[1], result[2], result[3])
        if result == "6174":
            break
    print(inum)
def more1(var1, var2, var3, var4):
    """more"""
    fst = most(var1, var2)
    fst = most(fst, var3)
    fst = most(fst, var4)
    if fst == var1:
        sec, trd, four = more2(var2, var3, var4)
    if fst == var2:
        sec, trd, four = more2(var1, var3, var4)
    if fst == var3:
        sec, trd, four = more2(var1, var2, var4)
    if fst == var4:
        sec, trd, four = more2(var1, var2, var3)*(fst == var4)
    return fst, sec, trd, four
def more2(var1, var2, var3):
    """more"""
    sec = most(var1, var2)
    sec = most(sec, var3)
    if sec == var1:
        trd, four = more3(var2, var3)
    if sec == var2:
        trd, four = more3(var1, var3)
    if sec == var3:
        trd, four = more3(var1, var2)
    return sec, trd, four
def more3(var1, var2):
    """more"""
    trd = most(var1, var2)
    if trd == var1:
        four = var2
    if trd == var2:
        four = var1
    return trd, four
def most(var1, var2):
    """most"""
    if var1 >= var2:
        return var1
    else:
        return var2
main()
