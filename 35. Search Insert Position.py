# 二分查找


from typing import List

'''
题目要求 O(log n)复杂度
就要考虑使用二分法

Runtime
0
ms
Beats
100.00%
Memory
19.90
MB
Beats
81.55%

'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1 item case
        # insert before head
        # insert after tail

        
        l = 0
        h = len(nums) - 1
        m = (l+h) // 2
        while l <= h:
            # print(l,m,h)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1
            m = (l + h) // 2

        print(l,m, h)
        #思考为什么搜索不到时返回位置是m+1
        #因为搜索不到时 h + 1 = l, 此时m = h, m = (l+h)//2 = (2h+1)//2 = h
        #插入位置就是 h和l之间即m+1或者说l
        # return m + 1 
        return l
        

'''
O(n)复杂度

Runtime
0
ms
Beats
100.00%
Memory
19.88
MB
Beats
81.55%

'''
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1 item case
        # insert before head
        # insert after tail

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i

        # insert at end
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1], 2))