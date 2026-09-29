def valid_parentheses(s: str) -> bool:
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False

            if pairs[char] != stack[-1]:
                return False

            stack.pop()

    return len(stack) == 0
  
print(valid_parentheses("())"))
# valid_parentheses("()")
# # True

# valid_parentheses("()[]{}")
# # True

# valid_parentheses("(]")
# # False

# valid_parentheses("([)]")
# # False

# valid_parentheses("{[]}")
# # True
