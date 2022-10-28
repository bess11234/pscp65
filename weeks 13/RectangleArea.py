"""RectangleArea"""
def main():
    """RectangleArea"""
    box_a, box_b = list(map(int, input().split())), list(map(int, input().split()))
    dx1 = box_a[0] + box_a[2]
    dy1 = box_a[1] + box_a[3]
    dx2 = box_b[0] + box_b[2]
    dy2 = box_b[1] + box_b[3]
    weight = max(0, min(dx1, dx2) - max(box_a[0], box_b[0]))
    height = max(0, min(dy1, dy2) - max(box_a[1], box_b[1]))
    result = weight*height
    if result == 0:
        print("no overlapping")
    else:
        print(result)
main()
