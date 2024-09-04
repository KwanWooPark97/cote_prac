dic={}
dic['000000']='A'
dic['001111']='B'
dic['010011']='C'
dic['011100']='D'
dic['100110']='E'
dic['101001']='F'
dic['110101']='G'
dic['111010']='H'

n=int(input())
a=input()
answer=''
li=[a[i*6:i*6+6] for i in range(n)]
for i in li:
    if i in dic:
        answer+=dic[i]
    else:
        for j in dic.keys():
            check=[]
            cnt=0
            for k in range(6):
                if i[k]!=j[k]:
                    cnt+=1
            if cnt<=1:
                answer+=dic[j]
                break
        else:
            print(li.index(i)+1)
            break
else:
    print(answer)
