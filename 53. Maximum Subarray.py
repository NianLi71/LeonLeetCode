

'''
比较直观
初始时f[i]=nums[i]
之后递推
f[i] = max(f[i-1]+nums[i], f[i])


'''
class Solution1:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        f = [0]*n
        for i in range(n):
            f[i] = nums[i]

        maxSum = f[0]
        for i in range(1, n):
            f[i] = max(f[i-1]+nums[i], f[i])
            if f[i] > maxSum:
                maxSum = f[i]

        return maxSum

'''
甚至可以简化，只保存f[i-1]作为lastSum
速度更快
'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)

        maxSum = nums[0]
        lastSum = nums[0]
        for i in range(1, n):
            lastSum = max(lastSum + nums[i], nums[i])
            if lastSum > maxSum:
                maxSum = lastSum

        return maxSum
            

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))