n=int(input())
st=[0]
for _ in range(n):
    st.append(int(input()))

a=[0]*(n+1)
b=[0]*(n+1)
a[1]=st[1]
b[1]=st[1]
for i in range(2,n+1):
    a[i]=max(a[i-2],b[i-2])+st[i]
    if i==2:
        b[i] = st[i] + st[i - 1]
    else:
        b[i]=max(b[i-3],a[i-3])+st[i]+st[i-1]

print(max(a[n],b[n]))