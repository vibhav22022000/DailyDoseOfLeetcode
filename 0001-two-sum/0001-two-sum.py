class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            sub = target - val
            if sub in seen:
                return [seen[sub], i]
            seen[val] = i
        
        
        