"""Key"""
def main(card):
    """Key"""
    key = 0
    for i in card:
        key += int(i)
    key += int(card[10:13])*10
    if len(str(key)) > 4:
        print(str(key)[1:5])
    elif key < 1000:
        print(key+1000)
    else:
        print(key)
main(input())
