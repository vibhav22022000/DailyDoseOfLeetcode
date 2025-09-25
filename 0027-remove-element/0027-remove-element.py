class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered = [num for num in nums if num != val]

        for i in range(len(filtered)):
            nums[i] = filtered[i]
        
        return len(filtered)

        