class Solution {
  int singleNumber(List<int> nums) {
    // Map<int,int> count = {};

    // for (var num in nums)
    // {
    //     count[num] = (count[num] ?? 0) + 1;
    // }

    // for (var entry in count.entries)
    // {
    //     if(entry.value == 1)
    //     {
    //         return entry.key;
    //     }
    // }
    // return -1;

    int result = 0;

    for (var num in nums)
    {
        result ^= num;
    }
    return result;
    
  }
}