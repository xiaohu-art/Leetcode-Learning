'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        nums = []
        nums = nums1 + nums2
        nums.sort()
        # p = q = 0
        # while ( p < m and q < n):
        #     if nums1[p] <= nums2[q]:
        #         nums.append(nums1[p])
        #         p += 1

        #     elif nums2[q] <= nums1[p]:
        #         nums.append(nums2[q])
        #         q += 1

        # if p == m:
        #     nums += nums2[q:]

        # elif q == n:
        #     nums += nums1[p:]

        return (nums[int((len(nums))/2)] + nums[int((len(nums))/2)-1])/2 if (len(nums) % 2) == 0  else nums[int((len(nums))/2)]


nums1 = [1,2]
nums2 = [3,4]
sol = Solution()
res = sol.findMedianSortedArrays(nums1, nums2)
print(res)
