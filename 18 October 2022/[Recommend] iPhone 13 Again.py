'''[Recommend] iPhone 13 Again'''
def main():
    '''[Recommend] iPhone 13 Again'''
    model = input().lower()
    storage = input()
    if model == "iphone 13 mini":
        print(check("mini", storage))
    elif model == "iphone 13":
        print(check("", storage))
    elif model == "iphone 13 pro":
        print(check("pro", storage))
    elif model == "iphone 13 pro max":
        print(check("max", storage))
    else:
        print("Not Available")
def check(model, store):
    """check"""
    if store == "128 GB":
        return 25900+4000*(model == "")+13000*(model == "pro")+17000*(model == "max")
    if store == "256 GB":
        return 29900+4000*(model == "")+13000*(model == "pro")+17000*(model == "max")
    if store == "512 GB":
        return 37900+4000*(model == "")+13000*(model == "pro")+17000*(model == "max")
    if store == "1 TB":
        if model == "pro" or model == "max":
            return 58900+4000*(model == "max")
        else:
            return "Not Available"
    return "Not Available"
main()
