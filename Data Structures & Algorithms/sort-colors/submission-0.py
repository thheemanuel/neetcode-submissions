class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        counts = [0, 0, 0]

        for n in range(0, len(nums)):
            counts[nums[n]] += 1
        
        i = 0

        for n in range(0, len(counts)):
            for j in range(0, counts[n]):
                nums[i] = n
                i += 1
        
        return nums