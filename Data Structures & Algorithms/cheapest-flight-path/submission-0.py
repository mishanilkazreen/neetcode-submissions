class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))

        fewest = [float("inf")] * n
        heap = [(0, src, 0)]

        while heap:
            cost, node, used = heapq.heappop(heap)
            if node == dst:
                return cost
            if used > k or used >= fewest[node]:
                continue
            fewest[node] = used
            for nb, w in adj[node]:
                heapq.heappush(heap, (cost + w, nb, used + 1))
        return -1