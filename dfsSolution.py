def solution(arr):
    total = 0

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[x][y] == 1:
                total += 1
                dfs(x,y,arr)
    return total

def dfs(x, y, arr):
    if x < 0 or x >= len(arr) or y < 0 or y >= len(arr[x]):
        return
    if arr[x][y] == 0:
        return
    arr[x][y] = 0
    dfs(x+1, y, arr)
    dfs(x-1, y, arr)
    dfs(x, y-1, arr)
    dfs(x, y+1, arr)

print(solution([[1,1,1],[1,0,0],[0,1,0]])) #2
