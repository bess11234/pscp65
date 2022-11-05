"""Gram_v1"""
def main():
    """Gram_v1"""
    text, dic = input(), {}
    start = 0
    stop = 2
    while stop <= len(text):
        if text[start:stop] not in dic:
            dic.update({text[start:stop] : 1})
        else:
            dic[text[start:stop]] += 1
        start += 1
        stop += 1
    for i in dic:
        if max(dic.values()) == dic[i]:
            print(i)
            print(max(dic.values()))
            break
main()
