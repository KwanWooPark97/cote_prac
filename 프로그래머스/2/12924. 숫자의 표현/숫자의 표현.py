def solution(n):
    answer = 0
    nums=[i for i in range(1,10001)]
    
    start=0
    end=1
    
    while start<end:
        now=sum(nums[start:end])
        if now<n:
            end+=1
        elif now>n:
            start+=1
        else:
            answer+=1
            end+=1
    
    return answer