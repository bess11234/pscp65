"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    text, lis, check = input().split(), [], ""
    for i in text:
        for j in i:
            if j in "aeiou":
                check += j
        if len(check) >= 2:
            lis.append(i.replace(".", ""))
        check = ""
    if lis == []:
        lis.append("Nope")
    print(*sorted(lis), sep="\n")
main()
