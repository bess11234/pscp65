"""pscp"""
def main():
    """pscp"""
    name1 = input()
    weight1 = float(input())
    height1 = float(input())
    bmi1 = weight1/(height1/100)**2
    name2 = input()
    weight2 = float(input())
    height2 = float(input())
    bmi2 = weight2/(height2/100)**2
    print(name1+"'s  BMI = %.2f"%bmi1)
    print(name2+"'s  BMI = %.2f"%bmi2)
    main2()
def main2():
    """2"""
    name3 = input()
    weight3 = float(input())
    height3 = float(input())
    bmi3 = weight3/(height3/100)**2
    name4 = input()
    weight4 = float(input())
    height4 = float(input())
    bmi4 = weight4/(height4/100)**2
    name5 = input()
    weight5 = float(input())
    height5 = float(input())
    bmi5 = weight5/(height5/100)**2
    print(name3+"'s  BMI = %.2f"%bmi3)
    print(name4+"'s  BMI = %.2f"%bmi4)
    print(name5+"'s  BMI = %.2f"%bmi5)
main()
