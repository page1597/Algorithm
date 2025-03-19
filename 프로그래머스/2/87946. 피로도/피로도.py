def solution(k, dungeons):
    max_count = 0 
    visited = [False] * len(dungeons)
    
    def backtrack(k, count):
        nonlocal max_count
        max_count = max(max_count, count)

        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k: 
                visited[i] = True  
                backtrack(k - dungeons[i][1], count + 1) 
                visited[i] = False  

    backtrack(k, 0)
    return max_count
