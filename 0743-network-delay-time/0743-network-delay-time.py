import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        
        pq = [(0, k)]
        distances = {}
        
        while pq:
            time, node = heapq.heappop(pq)
            
            
            if node in distances:
                continue
            
            distances[node] = time
            
            
            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(pq, (time + weight, neighbor))
                    
        
        if len(distances) == n:
            return max(distances.values())
        return -1
        