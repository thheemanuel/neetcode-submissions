class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #copy the given array over to a new one
        newList = nums

        for index in range(len(nums)):
            newList.append(nums[index])
        
        return newList