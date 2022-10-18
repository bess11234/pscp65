"""CuteCat CuteFox"""
def sub(animal):
    """sub"""
    animal = animal.replace("{", "").replace("}", "").replace(":", "")
    if animal[0] == "'":
        animal = animal.replace("'", "")
    elif animal[0] == '"':
        animal = animal.replace('"', "")
    return animal.split()
def main():
    """CuteCat CuteFox"""
    dic, dic2, row = {}, {}, [[1, "Cat01"], [1, "Fox01"]]
    cat = 0
    fox = 0
    txt_cat = ""
    txt_fox = ""
    total = ""
    for _ in range(int(input())):
        animal = input()
        animal = sub(animal)
        tmp, tmp2 = {animal[1] : animal[0]}, {animal[0] : animal[1]}
        dic.update(tmp)
        dic2.update(tmp2)
        if animal[1] == "Cat01" or animal[1] == "Fox01":
            continue
        tmp = animal[1].replace("Cat", "").replace("Fox", "")
        row.append([int(tmp), animal[1]])
    tmp = ""
    row.sort()
    while len(row) != 0:
        total = row[0][1]
        if total[:3] == "Cat":
            tmp = dic.get(total)
            if tmp == None:
                tmp = dic2.get("Garfield")
                if tmp == None and total == "Cat01":
                    txt_cat += "Garfield : %s\n"%total
                    cat += 1
            else:
                txt_cat += "%s : %s\n"%(tmp, total)
                cat += 1
        else:
            tmp = dic.get(total)
            if tmp == None:
                tmp = dic2.get("Fubuki")
                if tmp == None and total == "Fox01":
                    txt_fox += "Fubuki : %s\n"%total
                    fox += 1
            else:
                txt_fox += "%s : %s\n"%(tmp, total)
                fox += 1
        del row[0]
    print("Cat : %d"%cat)
    print("Fox : %d"%fox)
    print(txt_cat, end="")
    print(txt_fox, end="")
main()
