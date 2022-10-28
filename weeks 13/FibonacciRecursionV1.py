"""FibonacciRecursionV1"""
def fibo(num):
    """fiboเนี้ยแหละ"""
    if num <= 1:
        return num
    return fibo(num-1)+fibo(num-2)
def main():
    """FibonacciRecursionV1"""
    num = int(input())
    if num >= 2:
        num = fibo(num)
    print(num)
main()
