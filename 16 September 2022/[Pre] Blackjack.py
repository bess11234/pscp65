"""PRE"""
def main():
    """PRE"""
    num_card = int(input())
    value = 0
    count_a = 0
    special = "JQKA"
    for _ in range(num_card):
        card = input().upper()
        if special.count(card) >= 1:
            if card == "A":
                count_a += 1
            else:
                value += 10
        else:
            value += int(card)
    for _ in range(count_a):
        if value <= 10:
            value += 11
        else:
            value += 1
    if count_a > 0:
        if value > 21:
            value -= 10
    print(value)
main()
