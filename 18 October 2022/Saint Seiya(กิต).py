'''PSCP Program'''
def main():
    '''Saint Seiya'''
    print(method_two(int(input()), int(input())))
 
def method_two(req_time, req_atk):
    '''Super efficent O(n) solution'''
    type_1, type_2 = (req_time // 2 - req_time // 6), req_time // 6
    total_atk = (type_1*165) + type_2
    if total_atk < req_atk:
        return total_atk
    total_atk = (req_atk // 331) * 331
    temp_time = (total_atk // 331) * 6 # Every 6 seconds two 165 dmg atk and one 1 dmg atk happened
    if total_atk >= req_atk:
        temp_time += 1
    elif total_atk + 165 >= req_atk:
        total_atk += 165
        temp_time += 3
    elif total_atk + 330 >= req_atk:
        total_atk += 330
        temp_time += 5
    else:
        total_atk += 331
        temp_time += 6
    if req_time - temp_time > 0:
        total_atk += 12 * (req_time - temp_time)
    return total_atk
 
if __name__ == "__main__":
    main()
