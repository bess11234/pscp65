"""Median"""
def main():
    """Median"""
    num, lis = int(input()), []
    even = False
    index = num//2
    if num%2 == 0:
        even = True
    for _ in range(num):
        lis.append(int(input()))
    lis.sort()
    if even == False:
        print("%.1f"%lis[index])
    else:
        num = (lis[index-1]+lis[index])/2
        print("%.1f"%num)
main()
