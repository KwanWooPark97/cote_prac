def solution(storey):
    answer = 0
    while storey:
        a=storey%10
        storey=storey//10
        if a<5:
            answer+=a
        elif a>5:
            answer+=10-a
            storey+=1
        elif a==5:
            b=storey%10
            if b>=5:
                answer+=5
                storey+=1
            else:
                answer+=5
        
    return answer