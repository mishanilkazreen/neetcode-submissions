class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sub, used = [], [], set()

        def dfs(used):
            if len(used) == len(nums):
                # base case
                res.append(sub.copy())
                return
            
            for num in nums:
                if num in used: continue
                sub.append(num)
                used.add(num)
                dfs(used)
                sub.pop()
                used.remove(num)

        dfs(used)
        return res
