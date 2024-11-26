def solution(s):
    answer = []
    corpus=s.split(' ')
    for i in corpus:
        if i=='':
            answer.append(i)
            continue
        
        i=i.lower()
        if i[0].isalpha():
            i=i[0].upper()+i[1:]
        answer.append(i)
    
    return ' '.join(answer)