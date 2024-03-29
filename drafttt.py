def evaluate_expression(expression):
    def evaluate_tokens(tokens):
        operators = []
        numbers = []

        for token in tokens:
            if isinstance(token, float):
                numbers.append(token)
            elif token in ['+', '-', '*', '/', '%']:
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, numbers)
                operators.pop()

        while operators:
            apply_operator(operators, numbers)

        return numbers[0]

    def apply_operator(operators, numbers):
        operator = operators.pop()
        if operator == '+':
            num2 = numbers.pop()
            num1 = numbers.pop()
            numbers.append(num1 + num2)
        elif operator == '-':
            num2 = numbers.pop()
            num1 = numbers.pop()
            numbers.append(num1 - num2)
        elif operator == '*':
            num2 = numbers.pop()
            num1 = numbers.pop()
            numbers.append(num1 * num2)
        elif operator == '/':
            num2 = numbers.pop()
            num1 = numbers.pop()
            if num2 == 0:
                raise ValueError("Division by zero")
            numbers.append(num1 / num2)
        elif operator == '%':
            num2 = numbers.pop()
            num1 = numbers.pop()
            numbers.append(num1 * num2 / 100)

    def tokenize(expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(float(expression[i:j]))
                i = j
            elif expression[i] in ['+', '-', '*', '/', '(', ')', '%']:
                tokens.append(expression[i])
                i += 1
            else:
                i += 1
        return tokens

    tokens = tokenize(expression)
    return evaluate_tokens(tokens)

expression = "(2+3*2)-1"
result = evaluate_expression(expression)
print(result)
