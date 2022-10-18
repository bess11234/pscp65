"""BusStop I"""
def main():
    """BusStop I"""
    bus = []
    list_bus = []
    count = 0
    amount = int(input())
    stop = int(input())
    for _ in range(stop):
        event = input().split()
        event = list(map(int, event))
        list_bus.append(event)
    list_bus.sort()
    for i in range(stop):
        if bus.count(list_bus[i][0]) > 0:
            count += bus.count(list_bus[i][0])
            for _ in range(bus.count(list_bus[i][0])):
                bus.remove(list_bus[i][0])
        while len(list_bus[i]) != 1 and list_bus[i][0] != stop:
            if len(bus) == amount:
                break
            if list_bus[i][1] > list_bus[i][0] and not list_bus[i][1] > stop:
                bus.append(list_bus[i][1])
                del list_bus[i][1]
            else:
                del list_bus[i][1]
    print(count)
main()
