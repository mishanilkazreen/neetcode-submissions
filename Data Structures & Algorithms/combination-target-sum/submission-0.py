class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subarray = []

        def dfs(i, subarray, total):
            ## check if target or out of bounds
            if total == target:
                res.append(subarray.copy())
                return
            elif total > target:
                return
            if i >= len(nums):
                return
            
            # skip
            dfs(i+1, subarray, total)

            # reuse
            subarray.append(nums[i])
            total += nums[i]
            dfs(i, subarray, total)
            subarray.pop()
            
        dfs(0, subarray, 0)
        return res

            