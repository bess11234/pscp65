"""Day2011"""
def main():
    """Day2011"""
    day, month = int(input()), int(input())
    lis = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start = "Monday"*(month == 8)+"Tuesday"*(month == 2 or month == 3 or month == 11)+\
            "Wednesday"*(month == 6)+"Thursday"*(month == 9 or month == 12)+\
            "Friday"*(month == 4 or month == 7)+"Saturday"*(month == 1 or month == 10)+\
            "Sunday"*(month == 5)
    idx = lis.index(start)
    idx += (day-1)%7
    if idx >= 7:
        idx -= 7
    print(lis[idx])
main()
