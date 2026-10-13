class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subarray = []

        def dfs(i, total):
            # check if target is met
            if total == target:
                res.append(subarray.copy())
                return
            elif total > target or i >= len(candidates): 
                # check if out of bounds
                return

            # add number
            subarray.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subarray.pop()

            # skip
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, total)

        dfs(0 , 0)
        return res