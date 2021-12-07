import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = []
        
        for idx, ele in enumerate(self.nums):
            if ele == target:
                result.append(idx)
        return random.choice(result)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)