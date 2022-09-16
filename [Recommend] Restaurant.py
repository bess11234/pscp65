'''[Recommend] Restaurant'''
def main():
    '''[Recommend] Restaurant'''
    price = float(input())
    promo = float(input())
    percent = float(input())
    plus = float(input())
    cost = price+plus
    if promo <= price:
        price -= price*percent/100
    if cost >= promo:
        cost -= cost*percent/100
    if cost > price:
        print("No %.03f"%(cost-price))
    elif cost < price:
        print("Yes %.03f"%(price-cost))
    else:
        print("Yes")
main()
