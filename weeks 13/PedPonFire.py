"""PedPonFire"""
def main():
    """PedPonFire"""
    lis, num = [], int(input())
    for i in range(num):
        lis.append(int(input()))
    gas = int(input())
    count = 0
    lis = sorted(list(filter(lambda num: num <= gas, lis)))
    set_lis = set(lis)
    while True:
        if set_lis == set():
            break
        for i in set_lis:
            tmp = lis.count(i)
            tmp2 = gas-i
            if lis.count(tmp2) > 0:
                if tmp2 == i:
                    for j in range(tmp-1, 0, -1):
                        count += j
                    set_lis.remove(i)
                else:
                    count += lis.count(tmp2)*tmp
                    set_lis.remove(tmp2)
                    set_lis.remove(i)
                break
            else:
                set_lis.remove(i)
                break
    print(count)
main()
