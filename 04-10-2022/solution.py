'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        if len(l1) < len(l2):           # 保证 l1 更长
            tmp = l1
            l2 = l1
            l1 = tmp
        res = [0] * (len(l1)+1)
        for i in range(len(l2)):
            res[i] = l1[i] + l2[i]

        res[i+1:len(l1)] = l1[i+1:]
        for i in range(len(res)):
            if res[i-1] >= 10:
                res[i-1] %= 10
                res[i] += 1
        return res if res[-1] == 1 else res[:-1]

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]

l1 = [2,4,3]
l2 = [5,6,4]

sol = Solution()
print(sol.addTwoNumbers(l1, l2))