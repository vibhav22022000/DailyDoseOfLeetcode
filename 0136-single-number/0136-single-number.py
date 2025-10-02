class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #BEGINEER FRIENDLY DICT
        # count = {}

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # for num, freq in count.items():
        #     if freq == 1:
        #         return num
        
        # DEFAULT DICT
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        
        # for num,freq in count.items():
        #     if freq == 1:
        #         return num

        #XOR
        result = 0
        for num in nums:
            result ^= num
        
        return result