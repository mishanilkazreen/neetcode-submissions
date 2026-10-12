class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, -(y-x))

        return -heap[0] if heap else 0