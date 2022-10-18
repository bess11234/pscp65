'''Inflation'''
def main():
    '''Inflation'''
    price = float(input())
    year = int(input())
    price = int(price*100)
    for _ in range(year):
        digit = price*381
        price = price+digit//10000
    digit = str(price)[-2:]
    price = str(price)[:-2]
    if price == "":
        price = "0"
    print("%d.%02d"%(int(price), int(digit)))
main()
