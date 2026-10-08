class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = list(map(str, nums))
        
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if strs[i] + strs[j] < strs[j] + strs[i]:
                    strs[i], strs[j] = strs[j], strs[i]
        
        result = ''.join(strs)
        return '0' if result[0] == '0' else result