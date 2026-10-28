# https://leetcode.com/problems/contains-duplicate/

'''
思路
扫一遍数组，用一个set保存遍历过的元素，
如果一个元素已经在set中，就是有deplicate
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            numsSet.add(i)
        return False