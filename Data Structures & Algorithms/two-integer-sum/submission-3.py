class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #the solution which will be faster and use a hashmap

        map = {}

        for i in range(len(nums)):
            number = nums[i]
            complement = target - number

            if complement in map:
                return [map[complement], i]


            map[number] = i

        









