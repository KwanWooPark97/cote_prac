def solution(diffs, times, limit):
    answer = 0
    low=1
    high=max(diffs)
    while low<=high:
        time=times[0]
        mid=(low+high)//2
        for i in range(1,len(diffs)):
            if diffs[i]>mid:
                time+=((times[i-1]+times[i])*(diffs[i]-mid))+times[i]
            else:
                time+=times[i]
            if time>limit:
                low=mid+1
                break
        else:
            answer=mid
            high=mid-1

    
    return answer

'''
x



'''