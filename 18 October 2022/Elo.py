"""Elo"""
def main():
    """Elo"""
    rate_a = int(input())
    rate_b = int(input())
    person = input().upper()
    elo_a = elo(rate_b, rate_a)
    elo_b = elo(rate_a, rate_b)
    if person == "A":
        print("%.2f"%elo_a)
    else:
        print("%.2f"%elo_b)
def elo(rate1, rate2):
    """elo"""
    return 1/(1+10**((rate1-rate2)/400))
main()
