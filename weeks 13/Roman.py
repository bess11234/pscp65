"""Roman"""
def main():
    """Roman"""
    roman, total, before = input(), 0, 0
    value = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    while roman != "":
        if before >= value[roman[0]]:
            total += value[roman[0]]
            before = value[roman[0]]
            roman = roman[1:]
        elif before < value[roman[0]]:
            total = total-before*2+value[roman[0]]
            before = value[roman[0]]
            roman = roman[1:]
    print(total)
main()
