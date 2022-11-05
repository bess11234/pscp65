"""Scout"""
def main():
    """Scout"""
    for _ in range(int(input())):
        count = 0
        detail = list(map(int, input().split()))
        weight = list(map(int, input().split()))
        weight.sort()
        while True:
            if weight == []:
                break
            if 1 <= detail[1] and weight[0] <= detail[2]:
                count += 1
                detail[1] -= 1
                detail[2] -= weight[0]
                del weight[0]
            else:
                break
        print(count)
main()
