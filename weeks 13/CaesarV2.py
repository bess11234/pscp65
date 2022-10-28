"""CaesarV2"""
def check_result(result, common):
    """check"""
    for i in common:
        if i in result.lower():
            return True
    return False
def main():
    """CaesarV2"""
    import string
    common = ["what", "when", "why", "which", "this", "there", "where", "the"]
    text, a_z = input(), string.ascii_uppercase
    step = 0
    while True:
        result = ""
        for i in text:
            label = ""
            if i.isupper():
                idx = a_z.index(i)
                label = "u"
            elif i.islower():
                idx = a_z.lower().index(i)
                label = "l"
            idx += step
            idx = idx%26
            result += a_z[idx]*(label == "u")+a_z.lower()[idx]*(label == "l")+i*(label == "")
        if check_result(result, common):
            break
        step += 1
    print(result)
main()
