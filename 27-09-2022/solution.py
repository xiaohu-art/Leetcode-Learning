'''
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true 
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/check-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution_bak:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        flag = False
        s1 = list(s1)
        s1.sort()
        
        s2 = list(s2)
        s2.sort()

        flag = (''.join(s1) == ''.join(s2))

        return flag

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        else:
            Hash = [0] * 26
            for ch in s1:
                Hash[ord(ch) - ord('a')] += 1
            for ch in s2:
                Hash[ord(ch) - ord('a')] -= 1
                if Hash[ord(ch) - ord('a')] < 0:
                    return False
        
        return True

s1 = "asvnpzurz"
s2 = "urzsapzvn"
sol = Solution()
print(sol.CheckPermutation(s1, s2))