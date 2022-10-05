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
        if left == right:
            return 

        mid = (left + right) // 2
        self.mergesort(nums, left, mid, snums)
        self.mergesort(nums, mid+1, right, snums)
        self.merge(nums, left, mid, right, snums)
        return

    def merge(self, nums, left, mid, right, snums):
        i, j, pos = left, mid+1, left               # 分别指向左区间，右区间，有序列表

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                snums[pos] = nums[i]
                i += 1
            else:
                snums[pos] = nums[j]
                j += 1
            pos += 1
                                                    # 拷贝剩余元素
        while i <= mid:
            snums[pos] = nums[i]
            pos += 1
            i += 1

        while j <= right:
            snums[pos] = nums[j]
            pos += 1
            j += 1

        nums[left:right+1] = snums[left:right+1]    # 赋值回原数组

        return


    def reversePairs(self, nums):
        # 先写一个归并排序
        n = len(nums)
        snums = [0] * n

        self.mergesort(nums, 0, n-1, snums)         # 区间 左闭右闭

        return nums

         

nums = [7, 5, 6, 4]
sol = Solution()
print(sol.reversePairs(nums))

