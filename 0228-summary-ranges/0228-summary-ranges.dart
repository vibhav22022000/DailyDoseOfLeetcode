class Solution {
  List<String> summaryRanges(List<int> nums) {
    List<String> result = [];

    if (nums.isEmpty)
    {
        return result;
    }

    int start = nums[0]; 

    for (int i = 1; i < nums.length; i++)
    {
        if (nums[i] != (nums[i-1] + 1))
        {
            int end = nums[i-1];
            if (start == end)
            {
                result.add(start.toString());
            }
            else
            {
                result.add("$start->$end");
            }
            start = nums[i];
        }
    }

    int end = nums[nums.length - 1];
    if (start == end)
    {
        result.add(start.toString());
    }
    else 
    {
        result.add("$start->$end");
    }
    return result;

  }
}