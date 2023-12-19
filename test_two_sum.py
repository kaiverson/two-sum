import unittest
from solution import Solution

def compareAnswers(answer, expected):
  print(f"\n****************\nOutput:   {answer}\nExpected: {expected}\n****************")


class TestTwoSum(unittest.TestCase):
  def test_1(self):
    instance = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    answer = instance.twoSum(nums, target)
    compareAnswers(answer, expected)
    self.assertCountEqual(answer, expected)

  def test_2(self):
    instance = Solution()
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    answer = instance.twoSum(nums, target)
    compareAnswers(answer, expected)
    self.assertCountEqual(answer, expected)

  def test_3(self):
    instance = Solution()
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    answer = instance.twoSum(nums, target)
    compareAnswers(answer, expected)
    self.assertCountEqual(answer, expected)


if __name__=="__main__":
  unittest.main()
