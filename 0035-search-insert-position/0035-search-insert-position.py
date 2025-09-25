class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # BINARY SEARCH APPROACH O(Log n)
      
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return left


        # LINEAR SCAN VERSION O(n)

        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        
        # return len(nums)

        