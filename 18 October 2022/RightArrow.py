"""RightArrow"""
def main():
    """RightArrow"""
    length = int(input())
    height = int(input())
    space = 0
    for i in range(height):
        if i >= height//2+1:
            space += 2
        print(" "*(i-space)+"*"*length)
main()
