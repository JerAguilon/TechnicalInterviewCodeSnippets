'''
Given a string and a set of characters, return the **smallest** substring that contains all of the characters in the set
'''

def solution(string, char_set):
    # Step 1 and 2
    left, right, best_score = 0, 0, float('inf')

    # Step 3a:  Generally, for sliding window, you often need a set or hashmap to track
    #           the characters/values you have in your substring/subarray
    # Step 3b: This is an auxiliary value that lets us cleanly look up the characters
    #          in char_set that we have found
    letter_map = {} # maps from character to number of occurences in the substring
    characters_encountered = 0 # when this is equal to len(char_set), we have a
                               # candidate substring
    # Step 4
    while right < len(string):
        curr_right = string[right]

        # Step 5
        if curr_right in char_set:
            letter_map[curr_right] =  letter_map.get(curr_right, 0) + 1
            if letter_map[curr_right] == 1:
                characters_encountered += 1
        right += 1

        # Step 6: If you have a new candidate substring (in this case we found all
        #    our letters, begin incrementing left until it is *invalid*
        if (characters_encountered == len(char_set)):
            while characters_encountered == len(char_set):
                curr_left = string[left]
                if curr_left in char_set:
                    letter_map[curr_left] -= 1
                    if letter_map[curr_left] == 0:
                        characters_encountered -= 1
                left += 1
            # Step 7: Finally! Update the best score if we have a new best.
            #    This new candidate substring is bounded by right - left + 1. Avoid
            #    off-by-one's by drawing an example out.
            best_score = min(best_score, right - left + 1)
    return best_score


print(solution("adddddbcbba", {'a','b','c'})) # should be 4
print(solution("abc", {'a','b','c'})) # should be 3
print(solution("abdddddcbeba", {'a', 'b', 'c'})) # should be 5
print(solution("abweweffawefcaaaaboiwuroqiwuroiueeeb", {'a', 'b', 'c'})) # should be 6
