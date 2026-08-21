class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1): #check the video, there is so much logic behind this
            temp = one
            one = one + two
            two = temp
        
        return one