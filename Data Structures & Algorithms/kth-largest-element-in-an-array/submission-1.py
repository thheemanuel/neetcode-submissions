class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        i = 1
        n = 0
        for n in range(len(nums)):
            for i in range(len(nums)):
                if nums[i] > nums[n]:
                    temp = nums[n]
                    nums[n] = nums[i]
                    nums[i] = temp
                    

        print(nums)
        return nums[-k]
