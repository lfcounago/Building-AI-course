import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    sum = 0
    for index in range(0, len(row1)):
        sum += abs(row1[index] - row2[index])
    return sum
    
def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    outerrowindex = 0
    for row in data:
        innerrowindex = 0
        for secondrow in data:
            if innerrowindex == outerrowindex:
                dist[outerrowindex, innerrowindex] = np.inf
            else:
                dist[outerrowindex, innerrowindex] = distance(row, secondrow)
            innerrowindex += 1
        outerrowindex += 1
            
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)