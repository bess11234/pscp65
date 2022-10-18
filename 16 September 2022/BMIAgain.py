"""pscp"""
def main():
    """pscp"""
    wei = int(input())
    hei = int(input())/100
    bmi = wei/hei**2
    if bmi >= 30:
        print("Obese")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    else:
        print("Underweight")
main()
