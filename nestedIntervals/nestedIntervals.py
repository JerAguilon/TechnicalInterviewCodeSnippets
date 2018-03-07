def solution(string):
    stack = []
    for letter in string:
        if isOpeningBracket(letter):
            stack.append(letter)
        elif isClosingBracket(letter):
            if len(stack) == 0:
                return False
            lastOpener = stack.pop()
            if not matches(letter, lastOpener):
                return False
    return len(stack) == 0

def isOpeningBracket(letter):
    return letter in {'{', '(', '['}

def isClosingBracket(letter):
    return letter in {'}', ')', ']'}

def matches(closer, opener):
    openToClose = {'{':'}', '[':']', '(':')'}
    return openToClose[opener] == closer

print(solution("(3+9{12+4})(25)")) # true
print(solution("3+9{12+4})(25)")) # false
