"""PRE"""
def main():
    """PRE"""
    num_boat = int(input())
    boat = input()
    sum1 = 0
    inum = 0
    listpartyboat = boat.split()
    listpartyboat = listpartyboat[:num_boat*2]
    listpartyboat = list(map(int, listpartyboat))
    listpartyboat = sorted(listpartyboat)
    listpartyboat = listpartyboat[::-1]
    for _ in range(2):
        del listpartyboat[0]
    listpartyboat = sorted(listpartyboat)
    for i in listpartyboat[1:len(listpartyboat):2]:
        boat1 = listpartyboat[inum]
        sum1 += abs(boat1-i)
        inum += 2
    print(sum1)
main()
