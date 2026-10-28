# https://leetcode.com/problems/combination-sum/

from typing import List

'''
题目大意
candidates = [2,3,5], target = 8
用candidates里的数字组合相加，结果为target，
找出所有组合，数字可以重复选取，比如
[[2,2,2,2],[2,3,3],[3,5]]
'''

'''
思路
不断枚举所有可能的组合，用dfs
注意做剪枝，过程中一旦sum > target就剪掉
同时先对输入排序，一旦sum > target, 后面的数字就不用选了，因为数字是递增的
'''



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # 先排序
        
        cand_len = len(candidates)
        
        comb_list = []
        def dfs(cur_comb, cur_sum, pos):
            if cur_sum == target:
                comb_list.append(cur_comb[:])
                return
            
            for i in range(pos, cand_len): # 同一个position可以使用多次
                if cur_sum + candidates[i] <= target:  # 剪枝 move condition here
                    cur_comb.append(candidates[i])
                    dfs(cur_comb, cur_sum+candidates[i], i)
                    cur_comb.pop()
         
        dfs([], 0, 0)
        return comb_list