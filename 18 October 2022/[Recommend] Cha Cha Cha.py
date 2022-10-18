'''[Recommend] Cha Cha Cha'''
def main():
    '''[Recommend] Cha Cha Cha'''
    from math import ceil
    amount = int(input())
    salary = 0
    for _ in range(amount):
        hour = ceil(float(input()))
        salary += hour*8720
    print(salary)
main()
