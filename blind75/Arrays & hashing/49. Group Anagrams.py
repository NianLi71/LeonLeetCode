# https://leetcode.com/problems/group-anagrams/

'''
思路直接，对每个string拆散了排序，
再构建一个以排序后string为key的dict如
{
    'abc': ['acb', 'cba'],
    ...
}
每一个key对应value list就是可以互相拼写的组合
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        map = defaultdict(list)

        # improved
        for str in strs:
            sortedStr = ''.join(sorted(list(str))) # string和list操作是重点
            map[sortedStr].append(str)

        # print(map)

        res = []
        for _, v in map.items():
            res.append(v)

        return res
