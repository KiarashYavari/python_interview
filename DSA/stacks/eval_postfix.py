tokens = ["2", "3", "+", "4", "*"]
def eval_postfix(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack[-1]
        
        
print(eval_postfix(tokens=tokens))
# This is actually a very important stack lesson: the stack itself stores the intermediate results, 
# so you usually don't need a separate result variable that carries state across iterations.
