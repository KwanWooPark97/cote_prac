while 1:
    a=input()
    if a=='end':
        break
    mo=['a','e','i','o','u']
    for i in mo:
        if a.find(i)!=-1:
            break
    else:
        print('<'+a+'>'+' is not acceptable.')
        continue

    if len(a)>=3:
        for i in range(len(a)-2):
            cnt=0
            if a[i] not in mo and a[i+1] not in mo and a[i+2] not in mo:
                print('<' + a + '>' + ' is not acceptable.')
                break
            elif a[i] in mo and a[i+1] in mo and a[i+2] in mo:
                print('<' + a + '>' + ' is not acceptable.')
                break
        else:
            cnt=1
        if cnt==0:
            continue
    for i in range(len(a)-1):
        cnt=0
        if a[i] !='e' and a[i] !='o' and a[i]==a[i+1]:
            print('<' + a + '>' + ' is not acceptable.')
            break
    else:
        cnt=1
    if cnt==0:
        continue
    print('<'+a+'>'+' is acceptable.')