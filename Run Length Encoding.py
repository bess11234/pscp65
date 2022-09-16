"""Run Length Decoding"""
def main(text):
    """Run Length Decoding"""
    inum = 0
    while inum <= len(text)-1:
        count = 1
        jnum = inum
        while jnum < len(text)-1:
            if text[jnum] == text[jnum+1]:
                count += 1
                jnum += 1
            else:
                break
        print("%d%s"%(count, text[inum]))
        inum = jnum+1
main(input())
