
def solution(begin, end):
    answer = []
    def find_prime(n):
        cnt=[]
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                cnt.append(i)
                cnt.append(n//i)
        cnt.sort()
        if len(cnt)==0:
            return 1
        for i in cnt[::-1]:
            if i<=10000000:
                return i  
            
    for i in range(begin,end+1):
        if i==1:
            answer.append(0)
        else:
            answer.append(find_prime(i))
    return answer