def simpleRecrusion(weights,n,profits,maxCapacity):
    if maxCapacity == 0  or n == 0:
        return 0

    if (weights[n-1] > maxCapacity):
        return simpleRecrusion(weights, n-1, profits, maxCapacity)
    
    else:
        i = weights[n-1] + simpleRecrusion(weights,n-1,profits,maxCapacity-weights[n-1])
        j = simpleRecrusion(weights,n-1,profits,maxCapacity)
        ans = max (i,j)
        return ans

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(simpleRecrusion(wt, n, val, W))