"""CaesarV1"""
def main():
    """CaesarV1"""
    import string
    step, text, result, a_z = int(input()), input(), "", string.ascii_uppercase
    step = step%(26*(step >= 0)-26*(step < 0))
    for i in text:
        count, idx, label = 0, 0, ""
        if i.isupper():
            idx = a_z.index(i)
            label = "u"
        elif i.islower():
            idx = a_z.lower().index(i)
            label = "l"
        while count != step:
            if i not in a_z and i not in a_z.lower():
                break
            idx = idx+(1*(step >= 0)-1*(step < 0))
            if step < 0 and idx < 0:
                idx = 25
            elif step >= 0 and idx > 25:
                idx = 0
            count = count+(1*(step >= 0)-1*(step < 0))
        result += a_z[idx]*(label == "u")+a_z.lower()[idx]*(label == "l")+i*(label == "")
    print(result)
main()
