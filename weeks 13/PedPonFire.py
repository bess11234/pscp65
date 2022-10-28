"""PedPonFire"""
def main():
    """PedPonFire"""
    dic, lis, lis2 = {}, [], []
    for i in range(int(input())):
        dic.update({i : int(input())})
    gas = int(input())
    count = 0
    for i in dic:
        for j in range(len(dic)):
            tmp = 0
            if i != j:
                tmp += dic[i]+dic[j]
            if tmp == gas:
                pi
                count += 1
    print(count)
main()
