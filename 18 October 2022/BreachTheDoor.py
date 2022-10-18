"""BreachTheDoor"""
def main():
    """BreachTheDoor"""
    import string
    txt, result = "", ""
    rule = string.ascii_lowercase+" "
    for i in input():
        if i in rule or i in rule.upper():
            txt += i
    txt = txt.split()
    for i in range(len(txt)):
        if len(txt[i]) > 6:
            result += txt[i]+" "
    print(result.strip())
main()
