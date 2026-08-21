class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left_pointer = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[left_pointer] = nums[r]
                left_pointer += 1
        return left_pointer