s=input()
t=input()
def dfs(new):
    if len(new)==0:
        return
    if new==s:
        print(1)
        exit(0)

    if new[-1]=='A':
        dfs(new[:-1])
    if new[0]=='B':
        dfs(new[1:][::-1])

dfs(t)
print(0)