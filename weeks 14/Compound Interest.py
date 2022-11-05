"""Compound Interest"""
def main():
    """Compound Interest"""
    money, interest, years = int(input()), float(input()), int(input())
    for _ in range(years):
        money += money*interest/100
    print("%.2f"%money)
main()
