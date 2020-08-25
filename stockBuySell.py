def maxProfit(prices):
    
    res = 0
    minP=((2**32)-1)
    for i in range(len(prices)):
        if prices[i] < minP:
            minP= prices[i]
            
        if prices[i]-minP > res:
            res =prices[i]-minP
            
    return res

prices = [7,1,5,3,6,4]
res = maxProfit(prices)
print(res)