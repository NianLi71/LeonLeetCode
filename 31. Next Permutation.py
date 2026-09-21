


'''
思路
先找出排列末尾的降序部分，比如
8,4,7,6,5,3,2,1
中7,6,5,3,2,1就是降序
但是4, 7破坏了降序，从降序中找出比4大的最小值是5
交换4,5的位置
8,5,7,6,4,3,2,1
之后对7,6,4,3,2,1 做reverse
8,5,1,2,3,4,6,7

如果所有数字都是降序了，那就是最后一个最大排序了，需要reverse成最小排序
'''
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        # print(i)

        # 最大排序情况 3,2,1 -> 1,2,3
        if i == 0:
            nums.reverse()
        else:
            k = i - 1 #破坏降序的位置
            j = n - 1
            while j > 0: # 找到最接近的最大值
                if nums[j] > nums[k]:
                    break
                j -= 1
            nums[k],nums[j] = nums[j], nums[k]
            # print(nums)
            nums[k+1:] = nums[-1:k:-1] # 对k后面的数字reverse
            # print(nums)



if __name__ == '__main__':
    s = Solution()

    nums = [4,2,3,1]
    s.nextPermutation(nums)
    print(nums)

    nums = [4,3,2,1]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,2,3]
    s.nextPermutation(nums)
    print(nums)

    nums = [3,2,1]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,1,5]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,5]
    s.nextPermutation(nums)
    print(nums)

    nums = [1]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,3,2]
    s.nextPermutation(nums)
    print(nums)