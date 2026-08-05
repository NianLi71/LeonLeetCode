from typing import List

'''
Runtime
1714
ms
Beats
29.43%
Memory
19.70
MB
Beats
81.55%
'''
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

'''
Runtime
3
ms
Beats
53.89%
Memory
20.98
MB
Beats
6.77%
'''
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]):
                d.get(nums[i]).append(i)
            else:
                d[nums[i]] = [i]

        for first_num, idx_list in d.items():
            second_num = target - first_num
            if second_num in d:
                if second_num == first_num:
                    if len(idx_list) > 1:
                        return idx_list[:2]
                    else:
                        continue
                else:
                    return [idx_list[0], d[second_num][0]]

'''
这里利用了一个小技巧，如果有多个相同的数字，map只保存最后一个, 
开始计算时从头扫nums list，如果遇到3+3=6的情况，第一个3的index没有在map中，而第二个index在map中，
返回两个index即可

Runtime
2
ms
Beats
56.55%
Memory
20.56
MB
Beats
17.44%
'''
class Solution3(object):
    def twoSum(self, nums, target):
        map = {} # num to index mapping
        for i, e in enumerate(nums):
            map[e] = i # 如果有多个相同的数字，只保存最后一个
        
        for i in range(len(nums)):
            if (target - nums[i]) in map and i !=  map[target - nums[i]]:
                return list([ i, map[target - nums[i]] ])


'''
一次hash遍历, 一边遍历一边构建hash，

Runtime
0
ms
Beats
100.00%
Memory
20.39
MB
Beats
57.90%

'''
class Solution:
    def twoSum(self, nums, target):
        d = {}
        n = len(nums)

        for i in range(n):
            first_num = target - nums[i]
            if (first_num in d):
                return [d[first_num] ,i]
            d[nums[i]] = i
        return []


if __name__ == '__main__':
    s = Solution()

    nums = [2,7,11,15]
    target = 26

    # nums = [3,2,4]
    # target = 6

    # nums = [3,3]
    # target = 6

    res = s.twoSum(nums, target)
    print(res)