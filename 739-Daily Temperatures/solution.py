class Solution:
    def dailyTemperatures(self, temps):
        """
        :type temps: List[int]
        :rtype: List[int]
        """
        results = [0] * len(temps)
        stack = []

        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index

            stack.append(i)

        return results