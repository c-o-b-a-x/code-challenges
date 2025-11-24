s = input("Input: ")

stack = []
valid = True

for x in s:
    if x == "(" or x == "[" or x == "{":
        stack.append(x)
    else:
        if x == ")":
            if len(stack) == 0 or stack[-1] != "(":
                valid = False
                break
            stack.pop()
        if x == "]":
            if len(stack) == 0 or stack[-1] != "[":
                valid = False
                break
            stack.pop()
        if x == "}":
            if len(stack) == 0 or stack[-1] != "{":
                valid = False
                break
            stack.pop()

if len(stack) != 0:
    valid = False

print(valid)
