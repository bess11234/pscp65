"""1-15"""
def main():
    """1-15"""
    sec = int(input())
    minute = sec//60
    sec = sec%60
    hour = minute//60
    minute = minute%60
    day = hour//24
    hour = hour%24
    print(day, hour, minute, sec)
main()
