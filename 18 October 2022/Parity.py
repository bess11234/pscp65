"""Parity"""
def main():
    """Parity"""
    binary = input()
    typ = input()
    total = 0
    for i in binary:
        if i == "1":
            total += 1
    if (total%2 == 0 and typ == "Even") or (total%2 == 1 and typ == "Odd"):
        binary += "0"
    else:
        binary += "1"
    print(binary)
main()
