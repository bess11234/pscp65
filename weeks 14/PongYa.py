"""PongYa"""
def main():
    """PongYa"""
    num = int(input())
    if num%3 == 0 or str(num)[-1] == "3":
        print("PONG")
    else:
        print(num)
main()
