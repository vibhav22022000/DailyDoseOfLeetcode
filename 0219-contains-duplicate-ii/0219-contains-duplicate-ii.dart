class Solution {
  bool containsNearbyDuplicate(List<int> nums, int k) {
    
    Map<int,int> lastSeen = {};

    for (int i = 0; i < nums.length; i++)
    {
        int num = nums[i];
        if (lastSeen.containsKey(num) && (i - lastSeen[num]!) <= k)
        {
            return true;
        }
        lastSeen[num] = i;
    }
    return false;
  }
}