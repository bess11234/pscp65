"""1-15"""
def main():
    """1-15"""
    millisec = 492137954293754252786
    sec = millisec//1000
    millisec = millisec%1000
    minute = sec//60
    sec = sec%60
    hour = minute//60
    minute = minute%60
    day = hour//24
    hour = hour%24
    print(day, hour, minute, sec, millisec)
main()
