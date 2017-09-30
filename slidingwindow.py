def solution(string, charSet):
    if len(string) == 0:
        return 0
    if len(charSet) == 0:
        return 0

    left = 0;
    right = 0;
    letterMap = {}
    charactersEncountered = 0;
    bestScore = float('inf')
    while (left < len(string) and right < len(string)):
        letterMap[string[right]] =  \
            letterMap[string[right]] + 1 \
            if string[right] in letterMap else 1
        if letterMap[string[right]] == 1 and string[right] in charSet:
            charactersEncountered += 1
        right += 1
        # we've encountered every letter, let's minimize!
        if (charactersEncountered == 3):
            while (charactersEncountered == 3):
                letterMap[string[left]] -= 1
                if letterMap[string[left]] == 0 and string[left] in charSet:
                    charactersEncountered -= 1
                left += 1
            bestScore = min(bestScore, right - left + 1)
    return bestScore


print(solution("adddddbcbba", {'a','b','c'})) # should be 4
print(solution("abc", {'a','b','c'})) # should be 3
print(solution("abdddddcbeba", {'a', 'b', 'c'})) # should be 5
print(solution("abweweffawefcaaaaboiwuroqiwuroiueeeb", {'a', 'b', 'c'})) # should be 6
