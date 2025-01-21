from collections import deque

# bfs
def solution(maps):
    answer = 0
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 범위 안에 있을 때만
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    queue.append((nx, ny)) # 방문
                    maps[nx][ny] = maps[x][y] + 1 # 방문 표시 -> +1 (count)
       
    if maps[len(maps)-1][len(maps[0])-1] == 1: # 도착지 방문 안되어있다면
        return -1
    else:
        answer = maps[len(maps)-1][len(maps[0])-1]
        
    return answer