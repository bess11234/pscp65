'''Ping'''
def main():
    '''Ping'''
    ping = ""
    command = input()
    input()
    if command[-1].isdecimal() == True:
        posi = command.index("ping")+5
        ping = command[posi:]
    server = input()
    if ping == "":
        posi1 = server.index("[")+1
        posi2 = server.index("]")
        ping = server[posi1:posi2]
    reveived = 0
    lost = 4
    reply_1 = input()
    reply_2 = input()
    reply_3 = input()
    reply_4 = input()
    reveived += rep(reply_1)
    reveived += rep(reply_2)
    reveived += rep(reply_3)
    reveived += rep(reply_4)
    lost -= reveived
    per_loss = str(int((lost/4)*100))
    print("Ping statistics for %s:"%ping)
    print("    Packets: Sent = 4, Received = %d, Lost = %d "%(reveived, lost)+\
          "("+per_loss+"% loss),")
    main2(reply_1, reply_2, reply_3, reply_4, lost)
def main2(reply_1, reply_2, reply_3, reply_4, lost):
    """ส่วนที่ 2"""
    ms1 = pin(reply_1)
    ms2 = pin(reply_2)
    ms3 = pin(reply_3)
    ms4 = pin(reply_4)
    most_ms = most(ms1, ms2)
    most_ms = most(most_ms, ms3)
    most_ms = most(most_ms, ms4)
    least_ms = least(ms1, ms2)
    least_ms = least(least_ms, ms3)
    least_ms = least(least_ms, ms4)
    average = 0
    total = 0
    if isinstance(ms1, int):
        total += ms1
        average += 1
    if isinstance(ms2, int):
        total += ms2
        average += 1
    if isinstance(ms3, int):
        total += ms3
        average += 1
    if isinstance(ms4, int):
        total += ms4
        average += 1
    if lost != 4:
        average = total//average
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms"%(least_ms, most_ms, average))
def rep(reply):
    """reply"""
    if reply.count("Reply") > 0:
        return 1
    else:
        return 0
def pin(reply):
    """Ping"""
    check = reply.count("time")
    check2 = reply.count("timed")
    if check == 1 and check2 == 0:
        posi = reply.index("time")+4
        posi2 = reply.index("ms")
        m_s = reply[posi:posi2]
        if m_s == "<1":
            m_s = 0
        else:
            m_s = int(m_s[1:])
        return m_s
    else:
        return "0"
def most(var, var2):
    """most"""
    if var == "0":
        return var2
    if var2 == "0":
        return var
    if var >= var2:
        return var
    else:
        return var2
def least(var, var2):
    """least"""
    if var == "0":
        return var2
    if var2 == "0":
        return var
    if var <= var2:
        return var
    else:
        return var2
main()
