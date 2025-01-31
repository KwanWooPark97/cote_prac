import copy

t=int(input())

def dfs(start,word):
    if int(start)==(n):
        check=''.join(word).replace(' ','')
        if eval(check)==0:
            print(''.join(word))
        return

    for i in [' ','+','-']:
        now=copy.deepcopy(word)
        now.append(i)
        idx=str(int(start)+1)
        now.append(idx)
        dfs(idx,now)



for _ in range(t):
    n=int(input())
    dfs('1',['1'])
    print('')

