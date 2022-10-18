"""Safe"""
import string
def main():
    """Safe"""
    a_z = string.ascii_uppercase
    safe, lock, count, count2 = input(), input(), 0, []
    for i in range(len(safe)):
        dex = a_z.index(safe[i])
        dex2 = a_z.index(safe[i])
        while True:
            if a_z[dex] == lock[i]:
                break
            elif a_z[dex2] == lock[i]:
                break
            dex += 1
            if dex == 26:
                dex = 0
            dex2 -= 1
            if dex2 == -27:
                dex = -1
            count += 1
        count2.append(count)
        count = 0
    print(sum(count2))
main()
