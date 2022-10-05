'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def mergesort(self, nums, left, right, snums):
        if  (right - left) == 1 :
            '''
            为了防止列表为空这里递归基的条件可以改成：
            left >= right
            '''
            return 0

        mid = (left + right) // 2
        lcnt = self.mergesort(nums, left, mid, snums)
        rcnt = self.mergesort(nums, mid, right, snums)
        if nums[mid-1] <= nums[mid]:                # 稍微加速归并排序
            return lcnt + rcnt
        ccnt = self.merge(nums, left, mid, right, snums)
        return lcnt + rcnt + ccnt

    def merge(self, nums, left, mid, right, snums):
        i, j, pos = left, mid, left               # 分别指向左区间，右区间，有序列表
        cnt = 0
        while i < mid and j < right:
            if nums[i] <= nums[j]:
                snums[pos] = nums[i]
                i += 1
            else:
                snums[pos] = nums[j]
                j += 1
                cnt += (mid-i)
            pos += 1
                                                    # 拷贝剩余元素
        while i < mid:
            snums[pos] = nums[i]
            pos += 1
            i += 1

        while j < right:
            snums[pos] = nums[j]
            pos += 1
            j += 1

        nums[left:right] = snums[left:right]    # 赋值回原数组

        return cnt


    def reversePairs(self, nums):
        # 先写一个归并排序
        n = len(nums)
        snums = [0] * n

        '''
        判断列表是否为空
        小于两个元素直接返回 0 即可
        '''

        if n <= 1:                                        
            return 0

        cnt = self.mergesort(nums, 0, n, snums)         # 区间 左闭右开

        return cnt

         

nums = [7, 5, 6, 4]
sol = Solution()
print(sol.reversePairs(nums))

