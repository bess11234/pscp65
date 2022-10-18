"""Sequence XII"""
def half_top(num):
    """Sequence XII"""
    inum = 0
    knum = num
    for _ in range(1, num+1):
        for k in range(knum, num):
            print("%02d "%k, end="")
        for j in range(num, inum, -1):
            print("%02d "%j, end="")
        inum += 1
        knum -= 1
        for i in range(inum+1, num+1):
            print("%02d "%i, end="")
        for ggg in range(num-1, knum, -1):
            print("%02d "%ggg, end="")
        print()
    half_bottom(num)
def half_bottom(num):
    """Half_bottom"""
    jnum = 2
    knum = num-1
    inum = num-2
    inum2 = 1
    lnum = num
    for _ in range(1, num):
        for j in range(jnum, num+1):
            print("%02d "%j, end="")
        for k in range(knum, inum, -1):
            print("%02d "%k, end="")
        for i in range(lnum, num+1):
            print("%02d "%i, end="")
        for ggg in range(knum, inum2, -1):
            print("%02d "%ggg, end="")
        jnum += 1
        inum2 += 1
        inum -= 1
        lnum -= 1
        print()
half_top(int(input()))
