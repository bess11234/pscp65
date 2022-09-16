"""FOR!F-Ball"""
def main(event):
    """FOR!F-Ball"""
    ball = 1
    count = 0
    length = len(event)
    position(event, ball, count, length)
def position(event, ball, count, length):
    """position"""
    posi = ""
    if count >= length:
        print(ball)
    else:
        posi = event[count]
    if posi == "A" and ball == 1:
        ball = 2
        count += 1
        position(event, ball, count, length)
    elif posi == "A" and ball == 2:
        ball = 1
        count += 1
        position(event, ball, count, length)
    elif posi == "B" and ball == 2:
        ball = 3
        count += 1
        position(event, ball, count, length)
    elif posi == "B" and ball == 3:
        ball = 2
        count += 1
        position(event, ball, count, length)
    elif posi == "C" and ball == 3:
        ball = 1
        count += 1
        position(event, ball, count, length)
    elif posi == "C" and ball == 1:
        ball = 3
        count += 1
        position(event, ball, count, length)
    elif not posi == "":
        count += 1
        position(event, ball, count, length)
main(input())
