class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer_1 = 1

        for pointer_2 in range(1, len(nums)):

            if nums[pointer_2] != nums[pointer_2 - 1]:
                nums[pointer_1] = nums[pointer_2]
                pointer_1 += 1
        
        return pointer_1


        