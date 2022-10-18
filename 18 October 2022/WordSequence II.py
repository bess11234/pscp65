"""WordSequence II"""
def main():
    """WordSequence II"""
    txt = input()
    txt2 = input()
    check, inum = "", 0
    while True:
        if check == txt2 and inum > max(len(txt), len(txt2)):
            break
        check = txt2[:inum]+txt[inum:]
        inum += 1
        print(check)
main()
