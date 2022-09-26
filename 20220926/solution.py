'''
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]
示例 2:

输入: [2,3]
输出: [1,4]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/missing-two-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from typing import List
from functools import reduce

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        N = len(nums) + 2
        exp = list(range(1, N+1)) + nums
        r = reduce( lambda x, y: x ^ y ,exp )
        r = (r & -r)
        num1 = num2 = 0
        for num in exp:
            if num & r:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]


nums = [1, 2, 3, 5, 7, 8]
sol = Solution().missingTwo(nums)
print(sol)