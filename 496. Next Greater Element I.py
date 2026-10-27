
'''
翻译一下题目
x是数组中一个元素， 需要在同一个数组中找到x右边第一个比x大的元素，
如果没有就返回-1

题目输入的num1就相当于多个x组成了一个数组
num1中所有的元素num2中都有
num1,num2中元素都是unique
'''

'''
思路
直接模拟
对于x in nums1：
1.在nums2中找个x元素
2.往右找第一个比x大的元素

'''

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def findNextGreater(i):
            limit = len(nums2)
            for j in range(limit):
                if nums2[j] == nums1[i]: # 1.找到元素
                    j += 1
                    while j < limit: # 找到右边第一个greater元素
                        if nums2[j] > nums1[i]:
                            return nums2[j]
                        j += 1
            return -1

        res = []
        for i in range(len(nums1)):
            res.append(findNextGreater(i))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(s.nextGreaterElement([2,4], [1,2,3,4]))