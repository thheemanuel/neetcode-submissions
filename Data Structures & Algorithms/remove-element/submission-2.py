class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        o = 0

        for a in range(len(nums)):

            if nums[a] != val:
                nums[o] = nums[a]
                o += 1
        return o