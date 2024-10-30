def evaluate_exp(exp: str) -> float:
    
    # AHAHA BODMAS
    def precedence(op: str) -> int:
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    # THE STUFF THAT YOU CODE
    def apply_operation(a: float, b: float, op: str) -> float:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ValueError("REALLY? No like, seriously? Want to start a debate on division by zero?")
            return a / b

    # THE STUFF THAT I CODE
    def eval_expression(tokens: list) -> float:
        values = []
        ops = [] # stack bish

        for token in tokens:
            if isinstance(token, float): # checking if token is of float value
                values.append(token)
            elif token in ('+', '-', '*', '/'):
                while (ops and precedence(ops[-1]) >= precedence(token)): # checking top of the stack and the current ops
                    if len(values) <2:
                        return "ERROR BISH! I NEED TWO NUMBERS AROUND AN OPERATOR!"
                    right = values.pop()
                    left = values.pop()
                    op = ops.pop()
                    values.append(apply_operation(left, right, op))
                ops.append(token)

        while ops: # for the remaining operand in stack
            if len(values) <2:
                return "ERROR BISH! I NEED TWO NUMBERS AROUND AN OPERATOR!"
            right = values.pop()
            left = values.pop()
            op = ops.pop()
            values.append(apply_operation(left, right, op))

        if len(values) != 1:
            return "ERROR BISH! \n 1. Only enter integer or float values \n"\
            "2. Only use + , - , * or /"
        return values[0]

    # gonna convert the expression into tokens
    tokens = []
    num = ''
    for char in exp:
        if char.isdigit() or char == '.': # '.' for floating points
            num += char  # since I took string as input, I gotta build the numbers aka OPERANDS
        else:
            if num: # if number is built
                tokens.append(float(num))  # convert to float and append
                num = '' # reset
            if char in ('+', '-', '*', '/'):
                tokens.append(char)  # append operator
    if num:
        tokens.append(float(num))  # append the last number

    return eval_expression(tokens)


