"""Island"""
def num_island(island, row, col):
    """เพิ่มความทรมานนนน"""
    count = 0
    for i in range(row):
        for j in range(col):
            count += add_posi(island, i, j, row, col)
    return count
def add_posi(island, row, col, limit_row, limit_col):
    """เพิ่มมันเข้าไปนั้นแหละ"""
    tmp, count = [], 0
    eight_direc = [[-1, -1], [1, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [0, -1], [0, 1]]
    if island[row][col] == 1:
        island[row][col] = 0
        for i in eight_direc:
            tmp.append([row+i[0], col+i[1]])
        for i in tmp:
            if i[0] in range(0, limit_row) and i[1] in range(0, limit_col):
                add_posi(island, i[0], i[1], limit_row, limit_col)
        count = 1
    return count

def main():
    """พอเถอะพอแล้วพอ"""
    num, lis = list(map(int, input().split())), []
    for _ in range(num[0]):
        lis.append(list(map(int, input().split())))
    print(num_island(lis, num[0], num[1]))
main()
