"""Muddled Menu"""
def main():
    """Muddled Menu"""
    menu = []
    tmp = []
    inum = 0
    while True:
        order = input()
        if order.upper() == "DONE":
            break
        if order.upper() == "CLOSED":
            menu = []
            break
        if order.upper() == "SOMETHING'S WRONG":
            menu = []
            continue
        if order.count("Can't do: ") == 1:
            order = order.replace("Can't do: ", "")
            while True:
                count = menu[inum].count(order)
                if count == 1:
                    del menu[inum]
                    inum = 0
                    break
                inum += 1
            continue
        order = order.split(" #")
        order.reverse()
        if order[0].isdecimal() == True:
            menu.insert(int(order[0])-1, order[1])
        else:
            menu.append(order[1])
    for i in range(len(menu)):
        tmp.append(menu[i].strip())
    print("Full Course:", tmp, "Reversed:", tmp[::-1])
main()
