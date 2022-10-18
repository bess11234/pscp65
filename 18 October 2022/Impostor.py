"""Impostor"""
def slit(_):
    """split"""
    if _[0] == '"':
        tmp = _.replace('"', "").split(" : ")
    else:
        tmp = _.replace("'", "").split(" : ")
    return tmp
def main():
    """Impostor"""
    dead = {}
    alive = {}
    impostor = 0
    while True:
        add = input()
        if add == "Start":
            break
        tmp = slit(add[1:-1])
        alive.update({tmp[0] : tmp[1]})
    while add == "Start":
        kill = input()
        if kill == "End":
            break
        dead.update({kill : alive.pop(kill)})
    for _ in alive.values():
        if _ == "Impostor":
            impostor += 1
    print("%s Impostor Remains\n***Alive***"%impostor)
    for i in sorted(alive):
        print("%s : %s"%(i, alive[i]))
    print("***Dead***")
    for i in sorted(dead):
        print("%s : %s"%(i, dead[i]))
main()
