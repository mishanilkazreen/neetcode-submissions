class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        k_elements = []
        for i in range(len(bucket)-1,0,-1):
            if len(bucket[i]) != 0:
                k_elements.extend(bucket[i][:k-len(k_elements)])
                if len(k_elements) == k:
                    break
        return k_elements



