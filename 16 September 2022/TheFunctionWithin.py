"""pscp"""
def main():
    """pscp"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    print(fff(fff(aaa)))
    print(ggg(fff(aaa-bbb)))
    print(hhh(fff(aaa+bbb), fff(aaa+ccc), ggg(fff(ddd**2))))
    print(iii(hhh(fff(aaa+bbb), fff(aaa-ccc), ggg(fff(ddd**2))), ggg(fff(aaa-bbb)), \
                  fff(fff(fff(fff(fff(ccc))))), ddd**8))
def fff(xxx):
    """f"""
    return xxx*2
def ggg(xxx):
    """g"""
    return 3*xxx**4 - xxx**3 + 2*xxx**2+10
def hhh(xxx, yyy, zzz):
    """g"""
    return (zzz+xxx)**2 - xxx*yyy + yyy**2
def iii(aaa, bbb, ccc, ddd):
    """g"""
    return (aaa**2+bbb**2-ccc**2)/(ddd**2-2*aaa*ddd+2*aaa)
main()
