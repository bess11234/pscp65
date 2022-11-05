"""Bowling-Reddit"""
def plus(event):
    """plus"""
    total = 0
    if len(event[0]) == 2:
        return int(event[0][0].replace("-", "0"))+int(event[0][1].replace("-", "0"))
    if len(event[0]) == 3:
        if event[0][0] == "X":
            total += int(event[0][0].replace("X", "10"))
            if event[0][2] == "/":
                total += 10
            else:
                total += int(event[0][1].replace("X", "10").replace("-", "0"))+\
                         int(event[0][2].replace("X", "10").replace("-", "0"))
        else:
            total += 10+int(event[0][2].replace("-", "0").replace("X", "10"))
    return total
def main():
    """Bowling-Reddit"""
    event = (input()+" S").split()
    count, score = 0, 0
    while count != 9:
        count += 1
        count2 = 0
        tmp = []
        while True:
            if event[count2].count("X") > 0 and count2 < 4 and count < 10:
                count2 += 1
            elif (event[count2].count("X") == 0 or count2 >= 4) and count2 != 0:
                tmp = event[:count2]
                count2 -= 1*(tmp[-1].count("X") > 1)
                count2 -= 1*(len(tmp[-1]) == 3 and tmp[-1].count("X") == 1)
                break
            elif event[count2].count("X") == 0 or count == 10:
                break
        if tmp != []:
            if count2 == 1:
                event[1] = event[1].replace("-", "0")
                score += 10+int(event[1][0].replace("X", "10"))+\
                         int(event[1][1].replace("X", "10").replace("/", "10"))
                score -= int(event[1][0].replace("X", "10"))\
                         *(event[1].count("/") > 0 and len(event[1]) <= 2)
                del event[0]
            if count2 == 2:
                score += 20+int(event[2][0].replace("-", "0").replace("X", "10").replace("S", "0"))
                del event[0]
            if count2 == 3 or count2 == 4:
                score += 30
                del event[0]
        else:
            if event[0].count("/") == 0:
                event[0] = event[0].replace("-", "0")
                score += int(event[0][0].replace("X", "10"))+int(event[0][1].replace("X", "10"))
                del event[0]
            else:
                score += 10+int(event[1][0].replace("-", "0").replace("X", "10"))
                del event[0]
    event = event[:-1]
    score += plus(event)
    print(score)
main()
