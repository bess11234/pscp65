"""Cat Parade"""
def main():
    """Cat Parade"""
    list_cat = []
    list_tmp = []
    list_all = []
    inum = 1
    total = ""
    while True:
        cat = input()
        if cat == "END":
            break
        if cat == "IT'S A DOG":
            del list_cat[-1]
            inum -= 1
            continue
        for i in cat+",":
            if i == ",":
                if list_all.count(total.strip()) == 0:
                    list_tmp.append(total.strip())
                    list_tmp.append(inum)
                    list_cat.append(list_tmp)
                    list_tmp = []
                inum += 1
                list_all.append(total.strip())
                total = ""
                continue
            total += i
    for i in range(len(list_cat)):
        count = list_all.count(list_cat[i][0])
        list_cat[i].append(count)
    list_cat.sort()
    for i in range(len(list_cat)):
        print(*list_cat[i])
main()
