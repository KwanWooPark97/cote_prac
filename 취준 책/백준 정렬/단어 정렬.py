n=int(input())

data={}
for _ in range(n):
    n=str(input())
    r=len(n)
    if r not in data:
        data[r]=[n]
    else:
        if n not in data[r]:
            data[r].append(n)

key_list=list(data.keys())

key_list.sort()

for key in key_list:
    val=list(data[key])
    val.sort()

    for i in range(len(val)):
        print(val[i])
'''
import sys
n=int(sys.stdin.readline())
words=[]
for i in range(n):
    word=sys.stdin.readline().rstrip()
    words.append(word)
words=list(set(words))
words.sort()
words.sort(key=lambda x:len(x))
for i in words:
    print(i)
'''