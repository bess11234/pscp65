"""1-15"""
def main():
    """1-15"""
    val_x = int(input())
    val_y = int(input())
    val_z = int(input())
    print(one(val_x))
    print(two(val_y))
    print(three(val_z))
    print(four(val_x, val_y))
    print(five(val_x, val_y, val_z))
def one(val_x):
    """1"""
    return val_x+1
def two(val_y):
    """2"""
    return 7*(val_y**3)+2*(val_y**2)-31*(val_y)+1
def three(val_z):
    """3"""
    return -1*val_z
def four(val_x, val_y):
    """4"""
    return (val_x+val_y)*(val_x-val_y)
def five(val_x, val_y, val_z):
    """5"""
    import math
    one1 = val_y-math.sqrt(val_y**2-4*(val_x*val_z))
    two1 = 2*val_x
    return one1/two1
main()
