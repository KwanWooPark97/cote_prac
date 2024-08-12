def solution(n, t, m, timetable):
    answer = ''
    def h_to_m(times):
        h,m=times.split(':')
        return int(h)*60+int(m)
    tt=[]
    for i in timetable:
        tt.append(h_to_m(i))
    tt.sort()
    tt.reverse()
    bus=540-t
    for i in range(n-1):
        cnt=0
        bus=bus+t
        while len(tt)>=m and cnt!=m:
            if tt[-1]<=bus:
                tt.pop()
                cnt+=1
            else:
                break
    bus+=t
    if len(tt)<m:
        answer=bus
    elif len(tt)>=m:
        if tt[-m]<=bus:
            answer=tt[-m]-1
        else:
            answer=bus
    else:
        answer=bus
        
    answer=str(format(answer//60, '02'))+':'+(str(format(answer%60, '02')))
    return answer
