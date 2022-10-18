"""Solar System"""
def main():
    """Solar System"""
    hot = ""
    cool = ""
    solar = input()+" "
    sun = solar.index("Sun ")
    left, right = solar[:sun], solar[sun+4:]
    total_left, total_right = count_planet(left.strip()), count_planet(right.strip())
    if left != "":
        hot += planet_rever(left.strip())
    if right != "":
        hot += " "*(hot != "")+planet(right)
    if total_left == total_right:
        cool += planet(left)
        cool += " "+planet_rever(right.strip())
    if total_left > total_right:
        cool += planet(left)
    elif total_left < total_right:
        cool += planet_rever(right.strip())
    print("Hot: %s"%hot)
    print("Cool: %s"%cool)
def count_planet(solar):
    """count_planet"""
    total = 1
    if solar == "":
        total = 0
    for i in solar:
        if i == " ":
            total += 1
    return total
def planet_rever(solar):
    """planet"""
    ans = ""
    for i in solar[::-1]:
        if i == " ":
            break
        ans = i+ans
    return ans
def planet(solar):
    """planet"""
    ans = ""
    for i in solar:
        if i == " ":
            break
        ans += i
    return ans
main()
