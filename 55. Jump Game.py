

'''
用maxIndexCanBeReached去记录最远可到达的index值，
loop执行到i index时，
* 如果当前maxIndexCanBeReached是比i还远的话，就更新maxIndexCanBeReached,
* 否则maxIndexCanBeReached < i， 意味着目前的最远距离无法到达i
'''
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxIndexCanBeReached = 0
        for i in range(len(nums)):
            if maxIndexCanBeReached >= i:
                maxIndexCanBeReached = max(i + nums[i], maxIndexCanBeReached)
            else: # can not reach to index i
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))