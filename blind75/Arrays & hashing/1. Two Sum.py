# https://leetcode.com/problems/two-sum/


'''
思路
遍历数组的同时构造hash table d, d以数字为key, value是index
'''

class Solution:
    def twoSum(self, nums, target):
        d = {}
        n = len(nums)

        for i in range(n):
            first_num = target - nums[i] # target减去当前遍历的数字即是需要在数组中配对的数字first_num
            if (first_num in d): # first_name 已在d中
                return [d[first_num] ,i]
            d[nums[i]] = i
        return []