"""Phasmophobia"""
def check(evi_1, evi_2, evi_3):
    """check"""
    if evi_1 == "No evidence":
        evi_1 = evi_2
    if evi_1 == "No evidence":
        evi_1 = evi_3
    return evi_1
def main():
    """Phasmophobia"""
    ghosts = {"EMF Level 5" : ["Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"], \
              "Ghost Writing" : ["Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"], \
              "Fingerprints" : ["Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"], \
              "Spirit Box" : ["Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"], \
              "Freezing Temperatures" : ["Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"],\
              "Ghost Orb" : ["Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"], \
              "No evidence" : ["Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", "Poltergeist",\
                 "Revenant", "Shade", "Spirit", "Wraith", "Yurei"]}
    evi_1, evi_2, evi_3 = input(), input(), input()
    evi_1, evi_2, evi_3 = check(evi_1, evi_2, evi_3), check(evi_2, evi_3, evi_1), \
                          check(evi_3, evi_1, evi_2)
    found = set(ghosts[evi_1]) & set(ghosts[evi_2]) & set(ghosts[evi_3])
    if found == set():
        print("Not yet discovered")
    else:
        print(*sorted(list(found)), sep="\n")
main()
