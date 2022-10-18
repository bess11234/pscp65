"""Sequence XXX"""
def main():
    """Sequence XXX"""
    num1 = int(input())
    num2 = int(input())
    text = ""
    for i in range(num1):
        for j in range(num1):
            if i == 0 or i == num1-1 or j == 0 or j == num1-1 or i == j or j == num1-1-i:
                text += "*"
            else:
                text += " "
        text += " "
        print(text*num2)
        text = ""
main()
