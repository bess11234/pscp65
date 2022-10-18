"""BookWorm"""
def main():
    """BookWorm"""
    count = 0
    lis_read = []
    for _ in range(int(input())):
        time = float(input())
        for _ in range(int(input())):
            read = float(input())
            lis_read.append(read)
        lis_read.sort()
        for i in range(len(lis_read)):
            time -= lis_read[i]
            if time >= 0:
                count += 1
            else:
                break
        print(count)
        lis_read = []
        count = 0
main()
