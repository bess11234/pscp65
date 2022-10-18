"""PickThemAgain"""
def main():
    """PickThemAgain"""
    lis, lis2 = input().split(), []
    for i in lis:
        if int(i)%3 == 0 or int(i)%5 == 0:
            lis2.append(i)
    print(*lis2[::-1]*(lis2 != []), sep="\n", end="")
    print("Nope"*(lis2 == []), end="")
main()
