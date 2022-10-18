"""RemoveTag"""
def main():
    """RemoveTag"""
    txt = input()
    total = ""
    check = False
    for i in txt:
        if i == "<":
            total += " "
            check = True
        if i == ">":
            check = False
        elif check == False:
            total += i
    total = total.strip()
    if total != "":
        total = total.split()
        print(total)
    else:
        print("[]")
main()
