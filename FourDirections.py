'''FourDirections'''
def main():
    '''FourDirections'''
    direc = input()
    text = ""
    for j in direc:
        text += change(j, 1)
    print(text)
    text = ""
    for j in direc:
        text += change(j, 2)
    print(text)
    text = ""
    for j in direc:
        text += change(j, 3)
    print(text)
    text = ""
    for j in direc:
        text += change(j, 4)
    print(text)
    text = ""
    for j in direc:
        text += change(j, 5)
    print(text)
    text = ""
def change(text, num):
    """change"""
    if text == "D" and (num == 1 or num == 2 or num == 5) or \
       text == "U" and (num == 1 or num == 4 or num == 5) or \
       text == "L" and (num == 1 or num == 5) or \
       text == "R" and (num == 1 or num == 5):
        return "  *   "
    if text == "U" and num == 2 or text == "D" and num == 4:
        return " ***  "
    if text == "L" and (num == 2 or num == 4):
        return " *    "
    if text == "R" and (num == 2 or num == 4):
        return "   *  "
    if (text == "U" or text == "D") and num == 3:
        return "* * * "
    if (text == "L" or text == "R") and num == 3:
        return "***** "
main()
