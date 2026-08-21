class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        v = []

        subset = []

        def dfs(index):
            if index >= len(nums):
                v.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[index])
            dfs(index + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return v