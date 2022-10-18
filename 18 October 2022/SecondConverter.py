"""SecondConverter"""
def main():
    """SecondConverter"""
    my_sec = int(input())
    sec_c = int(input())
    mit_c = int(input())
    hour_c = int(input())
    mit = my_sec//sec_c
    sec = my_sec%sec_c
    hour = mit//mit_c
    mit = mit%mit_c
    hour = hour%hour_c
    print("%d:%d:%d"%(hour, mit, sec))
main()
