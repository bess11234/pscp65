"""Diamond I"""
def main():
    """Diamond I"""
    row = int(input())
    col = int(input())
    mine = []
    for _ in range(row):
        mining = input().split()
        mine.append(mining)
    tmp = 0
    most = 0
    for i in range(col):
        for j in range(row):
            tmp += int(mine[j][i])
        if tmp > most:
            most = tmp
        tmp = 0
    print(most)
main()
