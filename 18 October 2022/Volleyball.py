"""Volleyball"""
def main():
    """Volleyball"""
    event = input()+" "
    won_a = 0
    won_b = 0
    global_a = 0
    global_b = 0
    total = ""
    count = 0
    complete = False
    while len(event) != 0:
        for i in event:
            if (won_a >= 25 or won_b >= 25) and abs(won_a-won_b) >= 2 and count <= 3:
                complete = True
                break
            if count == 4 and (won_a >= 15 or won_b >= 15) and abs(won_a-won_b) >= 2:
                complete = True
                break
            if i == "A":
                won_a += 1
            elif i == "B":
                won_b += 1
            total += i
        count += 1
        if won_a > won_b:
            global_a += 1
        elif won_a < won_b:
            global_b += 1
        if count <= 5:
            print("Set %d: A (%d) | B (%d)"%(count, won_a, won_b))
        event = event.replace(total, "", 1)
        if count >= 4 and global_a-global_b != 0 and complete == True \
           or (abs(global_a-global_b) == 3):
            print("A won %d:%d set"%(global_a, global_b)*(global_a > global_b)+\
                  "B won %d:%d set"%(global_b, global_a)*(global_a < global_b))
            break
        complete = False
        won_a = 0
        won_b = 0
        total = ""
    if complete == False:
        print("The game has not finished yet.")
main()
