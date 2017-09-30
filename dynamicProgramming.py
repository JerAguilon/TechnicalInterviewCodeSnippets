def solution(n, coins):
    ascendingCoins = sorted(list(coins), reverse=True)
    total = 0
    for coin in ascendingCoins:
        total += solve(n - coin, ascendingCoins, coin)
    return total

cache = {}

def solve(n, coins, lastCoin):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for coin in coins:
        if coin <= lastCoin:
            total += solve(n - coin, coins, coin)
    cache[n] = total
    return total

def solveWithoutCache(n, coins, lastCoin):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for coin in coins:
        if coin <= lastCoin:
            total += solve(n - coin, coins, coin)
    return total

print(solution(15, {1,5})) # 4 ways
print(solution(1500, {150, 200, 300, 5, 20, 21, 51, 24, 35})) # won't terminate without cache
