def merge( intervals) :
    
    if len(intervals) == 0:
        return []
    
    if len(intervals) == 1:
        return intervals
    
    intervals = sorted(intervals, key = lambda x: x[0])
    
    res = [intervals[0]]
    
    for curr in intervals[1:]:
        prev = res[-1]
        
        if prev[1] >= curr[0]:
            prev[1] = max(prev[1], curr[1])
            
        else:
            res.append(curr)

    return res

arr = [[1,3],[2,6],[8,10],[15,18]]
res = merge(arr)
print(res)