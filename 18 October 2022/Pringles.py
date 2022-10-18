'''Pringles'''
def main():
    '''Pringles'''
    size_1 = input()
    lay = input()
    size_2 = input()
    hand = int(input())
    result = ""
    count1 = 0
    for i in lay[:hand]:
        if i == ")":
            result += " "
            count1 += 1
        else:
            result += " "
    result = result+lay[hand:]
    print(count1)
    if result.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(size_1, result, size_2, sep="\n")
main()
