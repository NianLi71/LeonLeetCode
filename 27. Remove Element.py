
'''
看似简单，但是计算挺精巧
特别是保存一个删除的次数变量，
i从前往后扫
j从后往前扫
如果从前面nums[i] == val, 就和后面nums[j]做一次交换， 此时保持i不动，j-=1
如果新从后面换来的nums[i]还是等于val,就在做一次和nums[j]交换，同时j-=1
每次nums[i], nums[j]就记一次删除操作，deleleTimes+=1
最后返回 n-deleleTimes , 即为剩下的数字个数
'''
class Solution1:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)

        i = 0
        j = n - 1
        deleleTimes = 0

        while i < n - deleleTimes: # i的范围限定在剩余数字个数中
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                deleleTimes += 1
            else:
                i += 1

        # print(nums)
        return n - deleleTimes

'''
我想复杂了，还有一种简单的方法
前k个元素保存删除后不等于val的数字，
从前往后扫描，如果遇到nums[i] != val, 就交换nums[k], nums[i], k+=1, k初始化为0
最终返回k
'''
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        print(nums)
        return k
       


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3],3))
    print(s.removeElement([0,1,2,2,3,0,4,2],2))
    print(s.removeElement([3,3,3,3],3))
    print(s.removeElement([2,3,3,3],3))