person={'Y':2,'F':3,'O':4}
n, game=input().split()
p=person[game]

lms=[input() for i in range(int(n))]

lms=list(set(lms))

print(len(lms)//(p-1))
