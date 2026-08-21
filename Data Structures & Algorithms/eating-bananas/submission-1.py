class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # initialize the left pointer to 1
        r = max(piles) # set the right pointer to the max value in the piles list
        res = r # at the minimum, the result will be the largest value in the piles list
        while l <= r: # while the pointers are in the correct order
            k = (l + r) // 2 # in binary search fashion we will have the bananas-per-hour rate be the "middle"
            hours = 0 # initialize the hours variable to 0
            for p in piles: # go throught each value in the piles list
                hours += math.ceil(p / k) # this calculates the hours it takes per pile and it rounds up, so if k = 2 and the pile is 3 it will take 2 hours to eat
            
            if hours <= h: # if the hours it took to eat all the bananas is less than the h, it is a correct answer to the question, but since we are interested in the minimum we will search again and move the right pointer to the left.
                res = min(res, k) # if the k value this time was less than last time, it means that we have a new minimum k to answer this question with, therefore we set the res variable to the new k
                r = k - 1 #move the right pointer to the left
            else:
                l = k + 1 #else, move the left pointer to the right
        
        return res #in the end of the loop, the res variable should contain the minimum k in order to eat all the bananas within the required time h.

        
        


