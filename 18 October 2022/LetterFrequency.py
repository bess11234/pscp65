"""LetterFrequency"""
def main():
    """LetterFrequency"""
    import string
    txt, txt2, num, result = "", [], 0, ""
    rule = string.ascii_lowercase
    for i in input().lower():
        if i in rule or i in rule.upper():
            txt += i
    txt = list(txt)
    for i in txt:
        if i not in txt2:
            txt2 += i
    for i in txt2:
        if txt.count(i) > num:
            num = txt.count(i)
            result = i
    print(result)
main()
