"""Stair"""
def main():
    """Stair"""
    step = int(input())
    stair = int(input())
    list1 = []
    count = 0
    for _ in range(stair):
        list1.append(int(input()))
    while True:
        inum = 0
        if list1[0] > step:
            print("NO")
            break
        for i in range(len(list1), 0, -1):
            if step >= sum(list1[:i]):
                inum = i
                break
        del list1[:inum]
        count += 1
        if len(list1) == 0:
            print(count)
            break
main()
