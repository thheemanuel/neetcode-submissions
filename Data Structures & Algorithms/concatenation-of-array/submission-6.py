class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #copy the given array over to a new one
        newList = nums

        #loop over the given array and for each integer stored at each index
        #append it to the new list, creating a list worthy of submission.
        for index in range(len(nums)):
            newList.append(nums[index])
        
        return newList