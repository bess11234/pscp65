"""B - Fully pair?"""
def main():
    """B - Fully pair?"""
    pair = input()
    char = ""
    for i in pair:
        if i not in char:
            char += i
    total = ""
    for i in char:
        if pair.count(i)%2 != 0:
            total += i
    if total == "":
        print("fully paired")
    else:
        print(total)
main()
