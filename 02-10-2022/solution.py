'''
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

 

示例 :

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/swap-adjacent-in-lr-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from sqlalchemy import false


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        p = q = 0
        if len(start) != len(end):
            return False
        else:
            n = len(start)
            while (p < n and q < n):
                while p < n and start[p] == 'X':
                    p += 1
                while q < n and end[q] == 'X':
                    q += 1

                # print(p, " ", q)
                if p < n and q < n:               # 边界情况
                    if start[p] != end[q]:
                        return False
                    
                    elif start[p] == 'R' and p > q:
                        return False
                    
                    elif start[p] == 'L' and p < q:
                        return False
                
                    p += 1
                    q += 1

            # 这里我忽略了一种情况就是 两个字符串的 L 和 R 的数量是不相同的；这样返回值应该是false
            while p < n:
                if start[p] != 'X':
                    return False
                p += 1
            while q < n:
                if end[q] != 'X':
                    return False
                q += 1
        return True


       

start = "RXXLRXRXL"
end = "XRLXXRRLX"
sol = Solution()
res = sol.canTransform(start, end)
print(res)