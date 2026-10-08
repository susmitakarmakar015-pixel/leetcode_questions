class Solution(object):
    def maxEvents(self, events):
        max_day = max(e[1] for e in events)
        parent = list(range(max_day + 2))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        events.sort(key=lambda e: e[1])
        
        count = 0
        for start, end in events:
            day = find(start)
            if day <= end:
                count += 1
                parent[day] = day + 1
        
        return count