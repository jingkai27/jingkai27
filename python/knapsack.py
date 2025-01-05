from typing import List

## Problem Setup:
## You have the following items:
## Item	Value (v), weight (w)
## item 1, v1=6 w1=1
## item 2, v2=10 w2=2
## item 3, v3=12 w3=3
# W = 5

def knapsack(values: List[int], weights: List[int], capacity: int) -> int:
    n = len(values)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    print(dp)
    # base case: dp[0] = [0,0,0,0,....,0]
    print(n)
    for i in range(1,n+1): 
        print("-----")
        print("i: ", i)
        for j in range(capacity+1): 
            if j < weights[i-1]: 
                dp[i][j] = dp[i-1][j]
            else: 
                dp[i][j] = max(dp[i-1][j-weights[i-1]]+values[i-1], dp[i-1][j])
    return dp[n][capacity]
          

values = [6, 10, 12]
weights = [1, 2, 3]
capacity = 5

print(knapsack(values, weights, capacity))

values = [20, 50, 30]
weights = [5, 10, 15]
capacity = 20
print(knapsack(values, weights, capacity))
