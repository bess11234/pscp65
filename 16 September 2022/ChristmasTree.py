"""ChristmasTree"""
def main(leaf, wood):
    """ChristmasTree"""
    inum = 1
    space = leaf-1
    for _ in range(leaf):
        print(" "*space+"*"*inum)
        inum += 2
        space -= 1
    space = leaf-2
    for _ in range(wood):
        print(" "*space+"---")
main(int(input()), int(input()))
