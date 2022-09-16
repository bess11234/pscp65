"""Grade III"""
def main(num):
    """Grade III"""
    import math
    total = 0
    for _ in range(num):
        score = float(input())
        if score >= 95:
            total += 4
        elif score >= 90:
            total += 3.5
        elif score >= 85:
            total += 3
        elif score >= 80:
            total += 2.5
        elif score >= 75:
            total += 2
        elif score >= 70:
            total += 1.5
        elif score >= 65:
            total += 1
        elif score >= 60:
            total += 0.5
        elif score >= 0:
            total += 0
    total = total/num
    print("%.2f"%(math.floor(total*100)/100.0))
main(int(input()))
