def solution(string, pattern):
    solution = [[False] * (len(string)+1) for _ in range(len(pattern)+1)]
    solution[0][0] = True
    for i in range(1, len(string)+1):
        solution[0][i] = True

    for i in range(1, len(pattern)+1):
        # as long as pattern is the empty string, let it matches
        solution[i][0] = solution[i-1][0] if pattern[i-1] == '*' else False
    for i in range(1, len(pattern)  + 1):
        for j in range(1, len(string) + 1):
            if matches(pattern[i - 1], string[j - 1]):
                solution[i][j] = solution[i-1][j-1]
            elif pattern[i - 1] == "*":
                solution[i][j] = True
            else:
                solution[i][j] = False
    return solution[len(pattern)][len(string)]

def matches(char1, char2):
    return char1 == '.' or char2 == '.' or char1==char2

print(solution("str", "st.*"))
print(solution("street", "s*at"))
