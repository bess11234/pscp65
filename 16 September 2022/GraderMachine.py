"""pscp"""
def main(start, stop):
    """pscp"""
    print("pass :", end="")
    total = 0
    if start <= stop:
        for i in range(start, stop+1):
            if i%2 == 0 and i != 0:
                print(" %d"%i, end="")
                total += i
    else:
        for i in range(start, stop-1, -1):
            if i%2 == 0 and i != 0:
                print(" %d"%i, end="")
                total += i
    print("\nSum : %d"%total)
main(int(input()), int(input()))
