"""GasStations"""
def main():
    """GasStations"""
    goal, able, num = float(input()), float(input()), int(input())
    lis = [0.0]
    for _ in range(num):
        lis.append(float(input()))
    lis.append(goal)
    count = 0
    if able < goal:
        while True:
            tmp = 0
            if able == 0:
                break
            for _ in range(len(lis)):
                if len(lis) == 2 or goal <= 0:
                    break
                if tmp <= able:
                    goal -= abs(lis[0] - lis[1])
                    tmp += abs(lis[0] - lis[1])
                if tmp > able:
                    goal += abs(lis[0] - lis[1])
                    tmp -= abs(lis[0] - lis[1])
                    break
                del lis[0]
            if len(lis) == 2 or goal <= 0 or abs(lis[0] - lis[1]) > able:
                break
            count += 1
    lis = [lis[0], lis[-1]]
    if abs(lis[0]-lis[1]) == 0 or goal < 0 or (count == 0 and abs(lis[0]-lis[1]) <= able):
        print(count)
    elif abs(lis[0]-lis[1]) <= able and num != 0:
        print(count+1)
    else:
        print("depleted")
main()
