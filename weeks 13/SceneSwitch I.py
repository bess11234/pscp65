"""SceneSwitch I"""
def main():
    """SceneSwitch I"""
    switch, count, before, check = 0, 0, 0, 0
    while True:
        command = input()
        if command != "End":
            command = float(command)
            if command == 0:
                before = command
                switch = 1
                check = 1
            elif switch == 1:
                switch = 0
                before = command
            else:
                if abs(before-command) <= 6 and check == 1:
                    switch = 1
                    count += 1
                    check = 0
                else:
                    switch = 1
                    check = 1
        else:
            print(count)
            break
main()
