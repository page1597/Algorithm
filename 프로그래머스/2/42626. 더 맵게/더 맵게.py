import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    
    while len(scoville) > 1:
        first_popped = heapq.heappop(scoville)
        second_popped = heapq.heappop(scoville)

        if first_popped >= K:
            break
        
        count += 1
        mixed_scoville = first_popped + (second_popped * 2)
        
        heapq.heappush(scoville, mixed_scoville)
    if len(scoville) == 1 and scoville[0] < K:
        count = -1
    answer = count
    return answer