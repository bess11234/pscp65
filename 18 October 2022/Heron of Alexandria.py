"""Heron of Alexandria"""
def main():
    """Heron of Alexandria"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_s = (var_a+var_b+var_c)/2
    print("%.3f"%((var_s*(var_s-var_a)*(var_s-var_b)*(var_s-var_c))**0.5))
main()
