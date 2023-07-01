def dfs(s,w,info,land,candi):
    # 양의 최댓값 갱신
    global answer
    if answer < s:
        answer = s
    # 양이랑 늑대랑 같으면 리턴
    if s <= w:
        return
    # 갈 수 있는 곳 dfs 돌기
    m = len(candi)
    for i in range(m):
        c = candi[i]
        # candi에서 자신만 빼고 다음 후보군에 더해주기
        candi2 = land[c] + candi[i+1:] + candi[:i]
        if info[c] == 0:
            dfs(s+1,w,info,land,candi2)
        elif info[c] == 1:
            dfs(s,w+1,info,land,candi2)
    

def solution(info, edges):
    global answer 
    answer = 0
    n = len(info)
    land = [[] for _ in range(n)]
    for p,c in edges:
        land[p].append(c)
    
    candi = land[0]
    dfs(1,0,info,land,candi)
    
    return answer