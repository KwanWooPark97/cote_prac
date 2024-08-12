def solution(plans):
    answer = []
    def h_to_m(t):
        h,m=t.split(":")
        return int(h)*60+int(m)
    for i in range(len(plans)):
        plans[i][1]=h_to_m(plans[i][1])
        plans[i][2]=int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    q=[]
    for i in range(len(plans)-1):
        if plans[i+1][1]>=plans[i][1]+plans[i][2]:
            answer.append(plans[i][0])
            rest=plans[i+1][1]-plans[i][1]-plans[i][2]
            while q and rest>0:
                if q[-1][1] >rest:
                    q[-1][1]-=rest
                    break
                else:
                    n,b=q.pop()
                    answer.append(n)
                    rest-=b
        else:
            q.append([plans[i][0],plans[i][2]-plans[i+1][1]+plans[i][1]])
    answer.append(plans[-1][0])
    for i in q[::-1]:
        answer.append(i[0])
    return answer