"""ProgressiveTax"""
def main():
    """ProgressiveTax"""
    tax = int(input())
    if tax <= 150000:
        print(0)
    else:
        print(calcurator_tax(tax))
def calcurator_tax(tax):
    """calculator"""
    if tax > 4000000:
        return tax1(tax-4000000, 0)
    if tax > 2000000:
        return tax2(tax-2000000, 0)
    if tax > 1000000:
        return tax3(tax-1000000, 0)
    if tax > 750000:
        return tax4(tax-750000, 0)
    if tax > 500000:
        return tax5(tax-500000, 0)
    if tax > 300000:
        return tax6(tax-300000, 0)
    if tax > 150000:
        return tax7(tax-150000, 0)
def tax1(tax, total):
    """tax1"""
    total += int(tax*35/100)
    return tax2(4000000-2000000, total)
def tax2(tax, total):
    """tax2"""
    total += int(tax*30/100)
    return tax3(2000000-1000000, total)
def tax3(tax, total):
    """tax3"""
    total += int(tax*25/100)
    return tax4(1000000-750000, total)
def tax4(tax, total):
    """tax4"""
    total += int(tax*20/100)
    return tax5(750000-500000, total)
def tax5(tax, total):
    """tax4"""
    total += int(tax*15/100)
    return tax6(500000-300000, total)
def tax6(tax, total):
    """tax4"""
    total += int(tax*10/100)
    return tax7(300000-150000, total)
def tax7(tax, total):
    """tax4"""
    total += int(tax*5/100)
    return total
main()
