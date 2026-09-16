

'''
递归构建subset

利用nums index, 每次添加一个后续的nums[index]
中间结果也保存
'''
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        res = []
        limit = len(nums)

        def dfs(idx, subset):
            res.append(subset) #把中间过程也保存为subset
            for i in range(idx, limit):
                dfs(i+1, subset+[nums[i]]) # 从下一个index开始，继续构造subset

        dfs(0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([4,5,6]))
    print(s.subsets([1,2,3]))
    print(s.subsets([0]))