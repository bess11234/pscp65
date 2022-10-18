"""Meteorite"""
def main():
    """Meteorite"""
    wei = float(input())
    peice = int(input())
    least = float(input())
    shot = 0
    inum = 1
    while wei >= least:
        if shot == 0:
            shot = 1
            wei = wei/peice
        else:
            wei = wei/peice
            shot += peice**inum
            inum += 1
    print(shot)
main()
