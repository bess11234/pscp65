"""FibonacciRecursionV2"""
def fibo(start, num, dic):
    """fibo"""
    if start >= num+1:
        return dic[start-1]
    else:
        if start == 0 or start == 1:
            dic.update({start : start})
            fibo(start+1, num, dic)
        else:
            dic.update({start : dic[start-1]+dic[start-2]})
            dic.update({start+1 : dic[start+1-1]+dic[start+1-2]})
            dic.update({start+2 : dic[start+2-1]+dic[start+2-2]})
            dic.update({start+3 : dic[start+3-1]+dic[start+3-2]})
            dic.update({start+4 : dic[start+4-1]+dic[start+4-2]})
            dic.update({start+5 : dic[start+5-1]+dic[start+5-2]})
            dic.update({start+6 : dic[start+6-1]+dic[start+6-2]})
            dic.update({start+7 : dic[start+7-1]+dic[start+7-2]})
            dic.update({start+8 : dic[start+8-1]+dic[start+8-2]})
            dic.update({start+9 : dic[start+9-1]+dic[start+9-2]})
            fibo(start+10, num, dic)
def main():
    """FibonacciRecursionV2"""
    num, dic = int(input()), {}
    fibo(0, num, dic)
    print(dic[num])
main()
