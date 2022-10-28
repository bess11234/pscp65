"""ClockHands"""
def main():
    """ClockHands"""
    hour = int(input())
    mit = int(input())
    hour *= 5
    hour += mit/12
    hour %= 60
    print(mit <= hour < mit+1)
main()
