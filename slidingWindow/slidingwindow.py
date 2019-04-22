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
    while right < len(string):
        curr_right = string[right]
        if curr_right in charSet:
            letterMap[curr_right] =  letterMap.get(curr_right, 0) + 1
            if letterMap[string[right]] == 1:
                charactersEncountered += 1
        right += 1
        # we've encountered every letter, let's minimize!
        if (charactersEncountered == len(charSet)):
            # make the string 'invalid' again, and update
            # bestScorebefore continuing
            while (charactersEncountered == len(charSet)):
                curr_left = string[left]
                if curr_left in charSet:
                    letterMap[curr_left] -= 1
                    if letterMap[curr_left] == 0:
                        charactersEncountered -= 1
                left += 1
            bestScore = min(bestScore, right - left + 1)
    return bestScore


print(solution("adddddbcbba", {'a','b','c'})) # should be 4
print(solution("abc", {'a','b','c'})) # should be 3
print(solution("abdddddcbeba", {'a', 'b', 'c'})) # should be 5
print(solution("abweweffawefcaaaaboiwuroqiwuroiueeeb", {'a', 'b', 'c'})) # should be 6
