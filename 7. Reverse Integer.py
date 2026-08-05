class Solution:
    def reverse(self, x: int) -> int:
        up_limit = 2**31 -1
        lower_limit = -2**31
        # print(up_limit, lower_limit)
        
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        # str(12345)[::-1] -> '54321'
        rev = str(x)[::-1] 
        rev_integer = sign * int(rev)
        
        # print(rev_integer)
        
        # 检查范围
        if lower_limit > rev_integer or rev_integer > up_limit:
            return 0
        else:
            return rev_integer
        
        