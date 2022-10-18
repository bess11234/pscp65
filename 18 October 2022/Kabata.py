"""Kabata"""
def main():
    """Kabata"""
    for _ in range(int(input())):
        kabata = input()
        while kabata != "":
            if kabata[:5] == "bakka":
                kabata = kabata[5:]
            elif kabata[:2] == "ka" or kabata[:2] == "ba" or kabata[:2] == "ta":
                if kabata[:2] == "ba" and kabata[2:4] == "ka":
                    break
                kabata = kabata[2:]
            else:
                break
        print("yes"*(kabata == "")+"no"*(kabata != ""))
main()
