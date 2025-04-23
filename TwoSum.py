# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def TwoSum(nums, target):

    i_dict = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in i_dict:
            return [i, i_dict[diff]]
        i_dict[num] = i
    return []


print(TwoSum([2, 7, 11, 15], 9))
print(TwoSum([3, 2, 4], target=6))
print(TwoSum([3, 3], target=6))
