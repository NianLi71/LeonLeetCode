


'''
思路
从1开始不断迭代， 每次统计连续的相同数字有几个，之后用个数和数字组成新的数字
1 -> (1,1) 1个1
11 -> (2,1) 2个1
21 -> (1,2,1,1) 1个2，1个1
1211 -> (1,1,1,2,2,1) 1个1，1个2，2个1

不如2019年的代码直观
'''
class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"
        for loop in range(n-1):
            t = ""
            i = 0
            while i < len(s):
                count = 1
                while i < len(s) - 1 and s[i] == s[i+1]:
                    i += 1
                    count += 1 
                t += str(count) + s[i]
                i += 1
            s = t
            # print(t)
        
        return s

'''
2019年版本
'''
class Solution2019:
    def countAndSay(self, n: int) -> str:
        
        cs = [1]
        next_cs = []
        for th in range(n-1):  # n-1 round
            j = 0
            while j < len(cs):
                count = 1
                while j < len(cs) - 1 and cs[j] == cs[j+1]:  # count same number
                    j+=1
                    count += 1
                next_cs.extend([count, cs[j]])
                j+=1
            cs = next_cs
            next_cs = []
        
        cs =  ''.join([str(n) for n in cs])
            
        return cs
        


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))

    print(s.countAndSay(5))

    print(s.countAndSay(1))
