n=int(input())

word=[]
di={}
for _ in range(n):
    word.append((input().split()))
result=[]
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j][0].upper() not in di:
            di[word[i][j][0].upper()]=1
            word[i][j]='['+word[i][j][0]+']'+word[i][j][1:]
            break
    else:
        for j in range(len(word[i])):
            flag=False
            for k in range(len(word[i][j])):
                if word[i][j][k].upper() not in di:
                    di[word[i][j][k].upper()] = 1
                    word[i][j] = word[i][j][:k]+'['+word[i][j][k]+']'+word[i][j][k+1:]
                    flag=True
                    break
            if flag:
                break
for i in range(n):
    print(' '.join(word[i]))