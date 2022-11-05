"""Rabbit"""
def main():
    """Rabbit"""
    rabbit, left_rabbit = int(input()), 0
    jump = int(input())
    carrot, left_carrot = int(input()), 0
    if rabbit > carrot:
        left_rabbit = rabbit-carrot
        rabbit -= left_rabbit
    elif carrot > rabbit:
        left_carrot = carrot-rabbit
    req_jump = int((rabbit*(rabbit+1)/2))
    tmp = 0
    if req_jump > jump:
        tmp = int((((2*jump)+(1/4))**(1/2))-(1/2))
        req_jump = int(jump-(tmp*(tmp+1)/2))
    if tmp != 0:
        left_rabbit += rabbit-tmp
        left_carrot += rabbit-tmp
    else:
        req_jump = jump-req_jump
    lis = [left_rabbit, req_jump, left_carrot]
    if lis.count(0) == 3:
        print("Ahhahaha")
    else:
        print(*lis)
main()
