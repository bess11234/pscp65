"""Saint Seiya"""
def main(req_sec, req_punch):
    """Saint Seiya"""
    punch = 0
    temp = 0
    for i in range(2, req_sec+1, 2):
        if punch < req_punch:
            if i%6 == 0:
                punch += 1
            elif i%2 == 0:
                punch += 165
        else:
            temp = req_sec+1-i
            break
    punch += temp*12
    print(punch)
main(int(input()), int(input()))
