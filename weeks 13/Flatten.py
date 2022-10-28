"""Flatten"""
def main():
    """Flatten"""
    import json
    lis, lis2 = json.loads(input()), []
    for i in lis:
        if isinstance(i, list):
            tmp = i
            tmp2 = []
            while tmp != []:
                for i in range(len(tmp)):
                    if isinstance(tmp[0], int):
                        lis2.append(tmp[0])
                        del tmp[0]
                    elif isinstance(tmp[0], list):
                        tmp2.extend(tmp[0])
                        del tmp[0]
                tmp.extend(tmp2)
                tmp2 = []
        else:
            lis2.append(i)
    print(sorted(lis2, reverse=True))
main()
