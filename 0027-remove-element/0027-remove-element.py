class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #TWO POINTER APPROACH
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


        #NEW LIST APPROACH
        # filtered = [num for num in nums if num!= val]

        # for i in range(len(filtered)):
        #     nums[i] = filtered[i]
        
        # return len(filtered)


        