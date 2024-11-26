def getMyDivisor(n,r):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            if i+n//i==r:
                return [n//i+2,i+2]

def solution(brown, yellow):
    answer = []
    if yellow==1:
        return [3,3]
    
    brown=brown//2-2
    answer=getMyDivisor(yellow,brown)
    answer.sort(reverse=True)
    return answer




'''
노란색 사각형 가로 x 세로 y라고 생각
갈색 2(x+2)+2y 만큼 필요 2(x+y+2)

가로 세로 갈색 노란색
3   3   3+3+2 1
4   3   4+4+2 1+1
4   4   4+4+2+2 2+2






'''