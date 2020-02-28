def nextval(T):
    length = len(T)
    next = length*[None]
    i,j = -1,0
    next[0] = -1
    while(j<length-1):
        if T[i] == T[j] or i == -1: #不要忘了初始i=-1
            i+=1
            j+=1
            if T[i] == T[j]:
                  """ 如果元素重复返回上一个next"""
                next[j] = next[i]
            else:
                next[j] =i
        else:
            i = next[i]
    return next

def find(T,S):
    next =nextval(T)
    a = 0
    b = 0
    while(a < len(T) and b< len(S)):
        if T[a] == S[b] or a == -1:
            a+=1
            b+=1
        else:
            a = next[a]
    if a == len(T):
        return b-len(T)
    else:
        return -1

t1 = "fjjjjjjjjj"
t2 = "fjalsfjlasdafjjjjjjjjjjjjjjj"
reuslt = find(t1,t2)
print(reuslt)
