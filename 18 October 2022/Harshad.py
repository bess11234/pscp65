"""Harshad"""
def main():
    """Harshad"""
    for _ in range(10):
        num = input()
        total = 0
        for i in str(num):
            if i == "-":
                pass
            else:
                total += int(i)
        if total == 0:
            print("No")
        elif int(num)%total == 0:
            print("Yes")
        else:
            print("No")
main()
