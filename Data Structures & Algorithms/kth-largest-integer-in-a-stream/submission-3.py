class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)

        i = 1


        for n in range(len(self.nums)):
            for i in range(len(self.nums)):
                if self.nums[i] > self.nums[n]:
                    temp = self.nums[n]
                    self.nums[n] = self.nums[i]
                    self.nums[i] = temp
        
        return self.nums[-self.k]



