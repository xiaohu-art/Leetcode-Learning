'''
给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

arr[0], arr[1], ..., arr[i] 为第一部分；
arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/three-equal-parts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from itertools import accumulate

class Solution(object):
    def threeEqualParts(self, arr):
        n = sum(arr)
        if n == 0:
            return [0, len(arr)-1]
        elif n % 3:
            return [-1, -1]
        
        partial = n / 3
        # acc = list(accumulate(arr))
        # first, second, third = acc.index(1), acc.index(partial+1), acc.index(partial*2+1)
        first, second, third, cur = 0, 0, 0, 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == 2 * partial:
                    third = i
                cur += 1


        length = len(arr) - third           # 二进制数长度
        if first + length <= second and second + length <= third:
            if arr[first: first+length] != arr[third:] or arr[second: second+length] != arr[third:]:
                return [-1, -1]
            else:
                return [first+length-1, second+length]
        return [-1, -1]

# arr = [0, 0, 0]
# arr = [1, 1, 0, 1, 1]
# arr = [1, 0, 1, 0, 1]
arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0]
sol = Solution()
print(sol.threeEqualParts(arr))
