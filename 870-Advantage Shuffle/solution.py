class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        sorted_nums2 = sorted(enumerate(nums2), key=lambda x: -x[1])
        
        result = [0] * len(nums1)
        lo, hi = 0, len(nums1) - 1
        
        for idx, val in sorted_nums2:
            if nums1[hi] > val:
                result[idx] = nums1[hi]
                hi -= 1
            else:
                result[idx] = nums1[lo]
                lo += 1
        
        return result