class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting Algorithm
        # result, count = 0,0

        # for n in nums:
        #     if count == 0:
        #         result = n
        #     count = (1 if n == result else -1)
        # return result
        
        #HASHMAP
        count = {}
        result, maxCount = 0,0

        for n in nums:
            count[n] = 1 + count.get(n,0)
            result = n if count[n] > maxCount else result
            maxCount = max(count[n], maxCount)
        
        return result
