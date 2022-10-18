"""PRE"""
def main():
    """PRE"""
    length = int(input())
    height = int(input())
    inum = height//2
    for _ in range(height//2):
        print(" "*inum+"*"*length, end="\n")
        inum -= 1
    inum = 1
    print("*"*length)
    for _ in range(height//2):
        print(" "*inum+"*"*length, end="\n")
        inum += 1
main()
