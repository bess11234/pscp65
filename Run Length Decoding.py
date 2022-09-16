"""Run Length Decoding"""
def main(text):
    """Run Length Decoding"""
    num = ""
    for i in text:
        if i.isalpha() == True:
            print(i*int(num), end="")
            num = ""
        else:
            num += i
main(input())
