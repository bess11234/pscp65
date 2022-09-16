"""RockPaperScissor"""
def main(event):
    """RockPaperScissor"""
    inum = 0
    total_a = 0
    total_b = 0
    a_list, b_list = [], []
    for i in event:
        if inum%2 == 0:
            a_list.append(i)
        if inum%2 == 1:
            b_list.append(i)
        inum += 1
    total_a, total_b = event1(a_list, b_list)
    if total_a > total_b:
        print("A win %d-%d"%(total_a, total_b))
    elif total_b > total_a:
        print("B win %d-%d"%(total_b, total_a))
    else:
        print("DRAW %d"%total_a)
def event1(a_list, b_list):
    """Event"""
    total_a = 0
    total_b = 0
    for i in range(len(a_list)):
        if a_list[i] == "R" and b_list[i] == "P":
            total_b += 1
        elif a_list[i] == "P" and b_list[i] == "R":
            total_a += 1
        elif a_list[i] == "S" and b_list[i] == "P":
            total_a += 1
        elif a_list[i] == "P" and b_list[i] == "S":
            total_b += 1
        elif a_list[i] == "R" and b_list[i] == "S":
            total_a += 1
        elif a_list[i] == "S" and b_list[i] == "R":
            total_b += 1
    return total_a, total_b
main(input())
