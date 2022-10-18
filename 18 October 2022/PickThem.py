"""PickThem"""
def main():
    """PickThem"""
    import json
    lis, lis2 = json.loads(input()), []
    for i in lis:
        if int(i)%2 == 0:
            lis2.append(i)
    print(*lis2*(lis2 != []), sep="\n", end="")
    print("Nope"*(lis2 == []), end="")
main()
