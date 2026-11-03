# https://leetcode.com/problems/word-break/

'''
题目大意
给一个字典, 和一个字符串
判断字符串能否用空格划分后, 使用字典中的单词完全拼写出来
'''

'''
思路dp
f[i]保存从s[i]递增到字符串结束能否用dict中单词组合出来

* f[i] = True if s[i:j+1] in dict and f[j+1]
* 边界条件f[len(s)] = True, 方便计算
意思是: 如果s[i..j](包含j)在字典中, 同时f[j+1] == True
那么f[i]也能用字典拼出来
'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        f[i] holds False or True, if from s[i] to end
        can be segmented using dict
        '''
        f = [False]*len(s)
        f.append(True) # 边界
        l = len(s)
        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if s[i:j+1] in wordDict and f[j+1]:
                    f[i] = True
                    break
        # print(f)
        return f[0]

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))