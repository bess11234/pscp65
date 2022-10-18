"""Seeker"""
def main():
    """Seeker"""
    total = ""
    cheat = input()
    for i in cheat:
        if i.isdecimal() == True:
            total += i
        else:
            total += " "
    total = total.split()
    print(sum(list(map(int, total))))
main()
