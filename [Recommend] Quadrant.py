"""pscp"""
def main():
    """pscp"""
    xxx = int(input())
    yyy = int(input())
    if xxx == 0 and yyy == 0:
        print("O")
    elif yyy == 0:
        print("X")
    elif xxx == 0:
        print("Y")
    elif xxx > 0 and yyy > 0:
        print("Q1")
    elif xxx < 0 and yyy > 0:
        print("Q2")
    elif xxx < 0 and yyy < 0:
        print("Q3")
    elif xxx > 0 and yyy < 0:
        print("Q4")
main()
