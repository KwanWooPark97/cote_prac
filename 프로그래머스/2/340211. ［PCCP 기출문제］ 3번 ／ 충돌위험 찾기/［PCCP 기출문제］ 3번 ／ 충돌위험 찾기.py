from collections import deque
from collections import defaultdict
from collections import Counter
import copy
def solution(points, routes):
    answer = 0
    path_list=[]
    def get_path(start_r, start_c, end_r, end_c, out_list=[]):

        now_r = start_r
        now_c = start_c

        while not (now_r == end_r and now_c == end_c):

            if now_r > end_r:
                now_r -= 1
                out_list.append((now_r, now_c))
                continue

            if now_r < end_r:
                now_r += 1
                out_list.append((now_r, now_c))
                continue

            if now_c > end_c:
                now_c -= 1
                out_list.append((now_r, now_c))
                continue

            if now_c < end_c:
                now_c += 1
                out_list.append((now_r, now_c))
                
    
    for i in range(len(routes)):
        temp=[]
        start=[points[routes[i][0]-1][0]-1,points[routes[i][0]-1][1]-1]
        temp.append(tuple(start))
        for j in range(1,len(routes[i])):
            end=[points[routes[i][j]-1][0]-1,points[routes[i][j]-1][1]-1]
            get_path(start[0],start[1],end[0],end[1],temp)
            start=end
        path_list.append(temp)
    
    max_len=0
    
    for i in range(len(routes)):
        max_len=max(max_len,len(path_list[i]))
        #print(path_list[i])
    for i in range(max_len):
        check=defaultdict(int)
        for j in range(len(routes)):
            if len(path_list[j])>i:
                check[path_list[j][i]]+=1
        for k in check.values():
            if k>=2:
                answer+=1
            
    return answer