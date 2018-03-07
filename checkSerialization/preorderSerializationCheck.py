def isValidSerialization(preorder):
    strings = preorder.split(",")
    stack = []
    for s in strings:
        stack.append(s)
        shouldCascade = True
        while (shouldCascade):
            if len(stack) < 3:
                shouldCascade = False
            else:
                top_1 = stack.pop()
                top_2 = stack.pop()
                top_3 = stack.pop()
                shouldCascade = top_1 == '#' and top_2 == '#' and top_3 != '#'

                if not shouldCascade:
                    stack.append(top_3)
                    stack.append(top_2)
                    stack.append(top_1)
                else:
                    stack.append('#')
    return len(stack) == 1 and stack.pop() == '#'
test = isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print(test) #True

test = isValidSerialization("9,#,#,1")
print(test) #False

