from collections import Counter
n=int(input())


for _ in range(n):
    m=int(input())
    d=list(map(int,input().split()))
    ds=Counter(d)
    score = {}
    for i in ds.keys():
        if ds[i]==6:
            score[i]=[]
    cnt=1
    for idx,team in enumerate(d):
        if team in score:
            score[team].append(cnt)
            cnt+=1
    s=[]
    t=[]
    for i in score.keys():
        s.append(sum(score[i][:4]))
        t.append(i)
    re=[]
    for i in range(len(s)):
        if s[i]==min(s):
            re.append(t[i])

    if len(re)>1:
        answer=[]
        for i in re:
            answer.append([score[i][4],i])
        answer.sort(key=lambda x:x[0])
        print(answer[0][1])
    else:
        print(re[0])



