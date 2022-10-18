"""pscp"""
def main():
    """pscp"""
    sec = int(input())
    minu, sec = sec//60, sec%60
    hour, minu = minu//60, minu%60
    day, hour = hour//24, hour%24
    if day >= 10000:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"%(day, hour, minu, sec))
main()
