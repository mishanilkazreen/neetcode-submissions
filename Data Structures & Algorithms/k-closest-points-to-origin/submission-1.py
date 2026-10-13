class Solution:
    def dist(self, x, y):
        return  math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for i in range(len(points)):
            x, y = points[i]
            heapq.heappush(res, (-self.dist(x, y), points[i]))
            while len(res) > k:
                heapq.heappop(res)
        return [p for _, p in res]

        