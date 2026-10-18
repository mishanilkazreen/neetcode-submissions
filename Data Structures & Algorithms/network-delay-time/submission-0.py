class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n+1)}

        for source, target, time in times:
            adjList[source].append((target, time))

        distances = {}
        heap = [(0, k)]
        while heap:
            distance, node = heapq.heappop(heap)

            if node in distances:
                continue
            
            distances[node] = distance
            for neighbour, time in adjList[node]:
                if neighbour not in distances:
                    heapq.heappush(heap, (distance+time, neighbour))

        return max(distances.values()) if len(distances) == n else -1