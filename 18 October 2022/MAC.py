"""MAC"""
def main():
    """MAC"""
    strict1 = "0123456789ABCDEF"
    strict2 = "-----", ":::::", ".."
    text = input().upper()
    num = 0
    check = 0
    special = ""
    for i in text:
        check += 1
        if i in strict1:
            num += 1
            continue
        if check == 3 or check == 6 or check == 9 or check == 12 or check == 15 \
           or check == 5 or check == 10:
            special += i
    if num != 12 or special not in strict2:
        print("ERROR")
    elif text.count("-") == text.count("-") == 5:
        print("VALID 1")
    elif text.count(":") == text.count(":") == 5:
        print("VALID 2")
    elif text.count(".") == text.count(".") == 2 and text[:4].isdecimal() == True:
        print("VALID 3")
    else:
        print("ERROR")
main()
