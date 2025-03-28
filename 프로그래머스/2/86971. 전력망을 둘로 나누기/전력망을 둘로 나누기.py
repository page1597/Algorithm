from collections import defaultdict

def solution(n, wires):
    answer = 10000
    tree = defaultdict(list)

    for wire in wires:
        tree[wire[0]] += [wire[1]]  # 노드 연결
        tree[wire[1]] += [wire[0]]

    for wire in wires:
        a, b = wire

		# 연결 끊어보기
        tree[a].remove(b)
        tree[b].remove(a)
        
        visited = set()

        count_a = travel_node(tree, a, visited)
        count_b = n - count_a # 잘라진 나머지 트리의 노드 개수
        
        answer = min(answer, abs(count_a - count_b))  # 최소 차이

		# 복구
        tree[a].append(b)
        tree[b].append(a)

    return answer

# 노드 개수 카운트
def travel_node(tree, node, visited):
    count = 1 
    visited.add(node) # 방문
    
    for neighbor in tree[node]:
        if neighbor not in visited:
            count += travel_node(tree, neighbor, visited)
    return count
