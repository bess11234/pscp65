"""Netflix"""
def main():
    """Netflix"""
    screen = int(input())
    phone = int(input())
    _ = input().title()
    _ = input().title()
    watch_tv = input().title()
    hdo = input().title()
    ultra = input().title()
    pre = 0
    stad = 0
    bsic = 0
    mob = 0
    total = 0
    while screen > 0 or phone > 0:
        if (ultra == "Yes" or hdo == "Yes" or watch_tv == "Yes") and (screen >= 3 or phone >= 3):
            total += 419
            pre += 1
            screen -= 4
            phone -= 4
        elif (hdo == "Yes" or watch_tv == "Yes") and (screen >= 2 or phone >= 2):
            total += 349
            stad += 1
            screen -= 2
            phone -= 2
        elif watch_tv == "Yes" and ultra == "No" and hdo == "No":
            total += 279
            bsic += 1
            screen -= 1
            phone -= 1
        else:
            if ultra == "Yes":
                total += 419
                pre += 1
                screen -= 4
                phone -= 4
            elif hdo == "Yes":
                total += 349
                stad += 1
                screen -= 2
                phone -= 2
            elif watch_tv == "Yes":
                total += 279
                bsic += 1
                screen -= 1
                phone -= 1
            else:
                total += 99
                mob += 1
                screen -= 1
                phone -= 1
    main2(pre, stad, bsic, mob, total)
def main2(pre, stad, bsic, mob, total):
    """main2"""
    if pre > 0:
        print("Premium x %d"%pre)
    if stad > 0:
        print("Standard x %d"%stad*(stad > 0))
    if bsic > 0:
        print("Basic x %d"%bsic*(bsic > 0))
    if mob > 0:
        print("Mobile x %d"%mob*(mob > 0))
    print("Total = %d THB"%total)
main()
