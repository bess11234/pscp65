"""pscp"""
def main():
    """pscp"""
    xxx = float(input())
    yyy = float(input())
    rrr = float(input())
    xnn = float(input())
    ynn = float(input())
    result = ((xxx-xnn)**2 + (yyy-ynn)**2)**0.5
    if result <= rrr:
        print(True)
    else:
        print(False)
main()
