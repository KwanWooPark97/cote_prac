a,p=map(int,input().split())

d=[a]

while True:
    answer=0
    for i in str(d[-1]):
        answer+=int(i)**p
    if answer in d:
        break
    d.append(answer)


print(len(d[:d.index(answer)]))

