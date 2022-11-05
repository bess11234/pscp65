"""CoinChangev1"""
def main():
    """CoinChangev1"""
    money = int(input())
    coin_25, money = money//25, money%25
    coin_10, money = money//10, money%10
    coin_5, money = money//5, money%5
    coin_1, money = money//1, money%1
    print(coin_25+coin_10+coin_5+coin_1)
main()
