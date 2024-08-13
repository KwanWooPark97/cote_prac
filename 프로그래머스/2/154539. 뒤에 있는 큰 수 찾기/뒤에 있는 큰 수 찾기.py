import heapq 
def solution(numbers):
    answer = []
    q=[]
    for idx,val in enumerate(numbers):
        if idx==0:
            heapq.heappush(q,[val,idx])
            continue
        while q and val>q[0][0]:
            _,ids=heapq.heappop(q)
            numbers[ids]=val
        heapq.heappush(q,[val,idx])
    while q:
        _,idx=heapq.heappop(q)
        numbers[idx]=-1
            
    return numbers