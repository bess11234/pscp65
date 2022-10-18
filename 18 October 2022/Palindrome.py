"""Palindrome"""
def main():
    """Palindrome"""
    wave = int(input())
    time = input()
    count = 0
    while count != wave:
        mit = "%02d"%(int(time[-2:])+1)
        hour = time[0:2].replace(":", "")
        if int(mit)%60 == 0 and int(mit) != 0:
            mit = "00"
            hour = str(int(hour)+1)
        if int(hour)%24 == 0:
            hour = "0"
        time = hour+":"+mit
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            count += 1
            print(time)
main()
