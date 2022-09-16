'''Bill'''
def main():
    '''Bill'''
    cost = int(input())
    service = cost*10/100
    if service <= 50:
        service = 50
    elif service > 1000:
        service = 1000
    cost = cost+service
    print("%.2f"%(cost*107/100))
main()
