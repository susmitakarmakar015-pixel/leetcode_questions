class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        r = []
        m = {}
        diff = []

        for num in arr2:
            if num not in m:
                m[num] = 0

        for num in arr1:
            if num in m:
                m[num] += 1
            else:
                diff.append(num)

        diff.sort()

        for num in arr2:
            r.extend([num] * m[num])

        r.extend(diff)

        return r