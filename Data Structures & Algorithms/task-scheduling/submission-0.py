class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        maxHeap = []
        for i in range(26):
            if freq[i] > 0:
                maxHeap.append(-freq[i])
        heapq.heapify(maxHeap)
        
        time, queue = 0, deque()
        while maxHeap or queue:
            time += 1

            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    queue.append([task, time+n])
            
            if queue and queue[0][1] == time:
                task = queue.popleft()[0]
                heapq.heappush(maxHeap, task)

        return time
