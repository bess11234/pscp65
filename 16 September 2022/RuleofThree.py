'''RuleofThree'''
def main():
    '''RuleofThree'''
    num = int(input())
    worth_p = 0
    worth_w = 0
    for _ in range(num):
        price = float(input())
        weight = float(input())
        if worth_p == 0:
            worth_p = price
            worth_w = weight
        elif worth_w/worth_p < weight/price:
            worth_p = price
            worth_w = weight
        elif worth_w/worth_p == weight/price:
            if price < worth_p:
                worth_p = price
                worth_w = weight
    print("%.2f %.2f"%(worth_p, worth_w))
main()
