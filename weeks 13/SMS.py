"""SMS"""
def main():
    """SMS"""
    sms = {1 : "Del", 2 : ["A", "B", "C"], 3 : ["D", "E", "F"], 4 : ["G", "H", "I"],\
           5 : ["J", "K", "L"], 6 : ["M", "N", "O"], 7 : ["P", "Q", "R", "S"],\
           8 : ["T", "U", "V"], 9 : ["W", "X", "Y", "Z"]}
    result = ""
    for _ in range(int(input())):
        button, press = int(input()), int(input())-1
        if button == 7 or button == 9:
            press %= 4
        elif (not button == 7 or not button == 9) and not button == 1:
            press %= 3
        if button == 1:
            for _ in range(press+1):
                result = result[:-1]
        else:
            result += sms[button][press]
    print(result*(result != "")+"null"*(result == ""))
main()
