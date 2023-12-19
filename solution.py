from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    numsMap = {}

    for i in range(len(nums)):
      compliment = target - nums[i]
      if (compliment in numsMap):
        return [numsMap[compliment], i]
      numsMap[nums[i]] = i

    # Program should never reach this point for inputs within constraints
    return []
