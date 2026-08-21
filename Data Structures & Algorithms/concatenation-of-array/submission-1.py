class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        newList = nums

        for index in range(len(nums)):
            newList.append(nums[index])
        return newList