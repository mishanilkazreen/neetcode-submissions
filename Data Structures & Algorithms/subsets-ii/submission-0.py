class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sub = [], []

        def dfs(i, sub):
            if sub not in res:
                res.append(sub.copy())
            if i >= len(nums): return

            dfs(i+1, sub)
            sub.append(nums[i])
            dfs(i+1, sub)
            sub.pop()
        
        dfs(0, sub)
        return res
