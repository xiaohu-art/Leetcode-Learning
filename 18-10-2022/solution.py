'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''

from re import I


class Solution():
    def trap(self, heights):
        h_idx = []

        res = 0
        for idx, height in enumerate(heights):
            while h_idx and height > heights[h_idx[-1]]:
                top = h_idx.pop()
                
                if not h_idx:
                    break
                left = h_idx[-1]
                width = idx - left - 1
                h = min(heights[left], heights[idx]) - heights[top]

                res += (width * h)
            h_idx.append(idx)
        
        return res


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(heights))