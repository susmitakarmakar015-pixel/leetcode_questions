class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))
        
        def mergeSort(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            
            merged = []
            i, j = left, mid + 1
            
            while i <= mid and j <= right:
                if nums[indices[i]] <= nums[indices[j]]:
                    counts[indices[i]] += j - (mid + 1)
                    merged.append(indices[i])
                    i += 1
                else:
                    merged.append(indices[j])
                    j += 1
            
            while i <= mid:
                counts[indices[i]] += j - (mid + 1)
                merged.append(indices[i])
                i += 1
            
            while j <= right:
                merged.append(indices[j])
                j += 1
            
            indices[left:right + 1] = merged
        
        mergeSort(0, n - 1)
        return counts