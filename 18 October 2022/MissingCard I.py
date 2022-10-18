"""MissingCard I"""
def main():
    """MissingCard I"""
    card = []
    for i in "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2":
        for j in "S", "H", "D", "C":
            card.append(i+j)
    for _ in range(51):
        have = input()
        card.remove(have)
    print(*card)
main()
