'''BigFrame'''
def main():
    '''BigFrame'''
    text1, text2, text3, text4, text5 = input().rstrip(), input().rstrip(), input().rstrip(), \
                                        input().rstrip(), input().rstrip()
    max1 = max(len(text1), len(text2), len(text3), len(text4), len(text5))
    print('**'*2+'*'*max1)
    for i in text1, text2, text3, text4, text5:
        print('* '+i+' '*(max1-len(i))+" *")
    print('**'*2+'*'*max1)
main()
