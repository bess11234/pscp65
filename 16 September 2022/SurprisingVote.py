"""SurprisingVote"""
def main(total, high):
    """SurprisingVote"""
    left = total-high
    if left > high:
        left -= high
        if high-left > 2:
            print("Surprising")
        else:
            print("Not surprising")
    elif high <= 2:
        print("Not surprising")
    else:
        print("Surprising")
main(float(input()), float(input()))
