class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num)
            while len(heap) > k:
                heapq.heappop(heap)
        return min(heap)