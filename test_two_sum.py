import unittest
from solution import Solution

class TestTwoSum(unittest.TestCase):
  def test_1(self):
    instance = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    solution = [0, 1]
    self.assertEqual(instance.twoSum(nums, target), expected)

def test_2(self):
    instance = Solution()
    nums = [3, 2, 4]
    target = 6
    solution = [1, 2]
    self.assertEqual(instance.twoSum(nums, target), expected)

def test_3(self):
    instance = Solution()
    nums = [3, 3]
    target = 6
    solution = [0, 1]
    self.assertEqual(instance.twoSum(nums, target), expected)


if __name__=="__main__":
  unittest.main()
