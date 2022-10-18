"""Lotto"""
def main():
    """Lotto"""
    price_1 = input()
    price_2 = input()
    price_3 = input()
    price_4 = input()
    price_5 = input()
    price_6 = input()
    my_price = input()
    price_1_1 = "%06d"%(int(price_1)+1)
    price_1_2 = "%06d"%(int(price_1)-1)
    won = 0
    if price_1 == "999999":
        price_1_1 = "000000"
        price_1_2 = "999998"
    if price_1 == "000000":
        price_1_1 = "000001"
        price_1_2 = "999999"
    if price_1 == my_price:
        won += 6000000
    if price_2 == my_price[4:6]:
        won += 2000
    if price_3 == my_price[:3]:
        won += 4000
    if price_4 == my_price[:3]:
        won += 4000
    if price_5 == my_price[3:6]:
        won += 4000
    if price_6 == my_price[3:6]:
        won += 4000
    if (price_1_1 == my_price) or (price_1_2 == my_price):
        won += 100000
    print(won)
main()
