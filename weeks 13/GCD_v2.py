"""GCD_v2"""
def main():
    """GCD_v2"""
    num, num2 = int(input()), int(input())
    while min(num, num2):
        num, num2 = min(num, num2), max(num, num2)%min(num, num2)
    print(max(num, num2))
main()
