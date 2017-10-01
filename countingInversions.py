def solution(arr):
    return countInversions(arr)

def countInversions(arr):
    # base case
    if len(arr) == 0 or len(arr) == 1:
        return 0

    # recursive case
    middle = len(arr) // 2
    left = arr[0:middle]
    right = arr[middle:]

    total = countInversions(left) + countInversions(right)

    i = 0
    pLeft = 0
    pRight = 0

    while (pLeft < len(left) and pRight < len(right)):
        if left[pLeft] <= right[pRight]:
            arr[i] = left[pLeft]
            pLeft += 1
        else:
            total += len(left) - pLeft
            arr[i] = right[pRight]
            pRight += 1
        i += 1
    while (pLeft < len(left)):
        arr[i] = left[pLeft]
        pLeft += 1
        i += 1
    while (pRight < len(right)):
        arr[i] = right[pRight]
        pRight += 1
        i += 1
    return total
import random
arr = [random.randint(0, 100) for i in range(100)]
print(solution(arr))
print(arr)

