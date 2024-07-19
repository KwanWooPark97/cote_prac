import math

def merge_sort(A):
    if len(A)==1:
        return A

    mid=math.ceil(float(len(A))/2.0)
    left=A[:mid]
    right=A[mid:]
    next_left=merge_sort(left)
    next_right=merge_sort(right)
    return merge(next_left,next_right)

def save_cnt(k):
    cnt.append(k[-1])

def merge(left,right):

    i=0
    j=0
    k=[]
    while(i < len(left) and j<len(right)):
        if left[i]<right[j]:
            k.append(left[i])
            i += 1
        else:
            k.append(right[j])
            j += 1
        save_cnt(k)
    while i<len(left):
        k.append(left[i])
        i +=1
        save_cnt(k)
    while j <len(right):
        k.append(right[j])
        j +=1
        save_cnt(k)
    return k


t,c=map(int,input().split())
cnt=[]
A=list(map(int,input().split()))

result=merge_sort(A)

if c > len(cnt):
    print('-1')
else:
    print(cnt[c-1])

