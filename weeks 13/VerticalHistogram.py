"""VerticalHistogram"""
def main():
    """VerticalHistogram"""
    text, count, label, dic_la = list(input()), 0, [], {}
    text.sort()
    for i in text:
        if i.isupper() == True:
            count += 1
    text = text[count:]+text[:count]
    for i in text:
        if i not in label:
            label.append(i)
    for i in label:
        dic_la.update({i : text.count(i)})
    for i in range(max(dic_la.values()), -1, -1):
        print("%03d"%i*(i != 0)+"   "*(i == 0), end="")
        for j in dic_la:
            if dic_la[j] >= i and i != 0:
                print(" *", end="")
            elif not dic_la[j] >= i and i != 0:
                print("  ", end="")
            if i == 0:
                print(" %s"%j, end="")
        print()
main()
