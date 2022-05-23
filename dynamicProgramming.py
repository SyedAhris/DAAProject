def dynamicProgramming(weights,n,maxCapacity):
    dpArr = [[0 for x in range(maxCapacity + 1)] for x in range(n + 1)]

    for i in range(0,n+1):
        for w in range (0, maxCapacity+1):
            if i == 0 or w == 0:
                dpArr[i][w] == 0
            elif weights[i-1] <= w:
                a = weights[i-1] + dpArr[i-1][w-weights[i-1]]
                b = dpArr[i-1][w]
                dpArr[i][w] = max(a,b)
            else:
                dpArr[i][w] = dpArr[i-1][w]
    
    return dpArr[n][maxCapacity]
