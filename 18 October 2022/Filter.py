"""Filter"""
def main():
    """Filter"""
    import json
    std = json.loads(input())
    fill = float(input())
    good = {}
    for i in sorted(std.keys()):
        if std[i] >= fill:
            good.update({i : "%.2f"%std[i]})
    if good == {}:
        print("Nope", end="")
    for i in good.keys():
        print(i, good[i], sep="\t")
main()
