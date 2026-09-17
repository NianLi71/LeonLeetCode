
'''
简单题，
nums[i]代表前i个index位置上已经是unique sorted numbers
枚举i后面j
if nums[j] != nums[i], 就把nums[j]放在nums[i+1]
'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        i= 0
        j = i+1

        while j < len(nums):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i = i+1
            j = j+1

        # print(nums)
        return i+1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1]))
    print(s.removeDuplicates([1,1]))
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4,4]))