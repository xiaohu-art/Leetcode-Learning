'''
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/get-kth-magic-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 最小堆
import heapq

class Solution_bak:
    def getKthMagicNumber(self, k):
        factors = [3, 5, 7]
        seen = {1}
        heap = [1]

        for i in range(k-1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

# 动态规划
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * k
        dp[0] = 1
        p3 = 0
        p5 = 0
        p7 = 0
        for i in range(1, k):
            dp[i] = min(dp[p3]*3, dp[p5]*5, dp[p7]*7)

            if dp[i] == dp[p3] * 3:
                p3 += 1
            
            if dp[i] == dp[p5] * 5:
                p5 += 1
            
            if dp[i] == dp[p7] * 7:
                p7 += 1
        
        return dp[-1]
            
 


k = 5
sol = Solution()
print(sol.getKthMagicNumber(k))