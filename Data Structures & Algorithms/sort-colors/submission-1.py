class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        counts = [0, 0, 0] #create the three buckets for "0,1,2"

        for n in range(0, len(nums)): # loop through the length of nums
            counts[nums[n]] += 1 # if nums[n] = 0 for example, that becomes the index in counts, and it is incremented by one
                                 # so basically, the buckets get incremented to the times they appear in the array nums.
        i = 0 #create an integer and set the value to 0

        for n in range(0, len(counts)): # loop through the count array, aka the buckets
            for j in range(0, counts[n]): # loop from zero to the value of every bucket slot. 
                                          # so if the bucket looks like this [2,3,2] the inner loop will execute two times
                                          # setting the beginning of the nums array to [0,0... because n is at zero and the loop will execute two times before returning to the outer loop to move to the next bucket.
                nums[i] = n # this sets the value of nums at the index i to the iteration of the outer loop aka "n"
                i += 1 # increment i by one, to move nums array pointer forward.
        
        return nums #return the sorted array nums.