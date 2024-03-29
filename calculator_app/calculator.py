def evaluate_expression(expression):
    def evaluate_subexpression(subexpression):
        operators = []
        numbers = []

        current_number = ''
        for sub_char in subexpression:
            if sub_char.isdigit() or sub_char == '.':
                current_number += sub_char
            else:
                if current_number:
                    numbers.append(float(current_number))
                    current_number = ''

                if sub_char in ['+', '-', 'x', '÷', '%']:
                    operators.append(sub_char)

        if current_number:
            numbers.append(float(current_number))

        i = 0
        while i < len(operators):
            if operators[i] in ['x', '÷']:
                num1 = numbers[i]
                num2 = numbers[i + 1]
                operator = operators.pop(i)

                if operator == 'x':
                    result = num1 * num2
                elif operator == '÷':
                    result = num1 / num2

                numbers[i] = result
                numbers.pop(i + 1)
            else:
                i += 1

        result = numbers[0]
        for i in range(len(operators)):
            operator = operators[i]
            num = numbers[i + 1]

            if operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator == '%':
                result *= num / 100

        return result

    def evaluate(expression):
        while '(' in expression:
            start = expression.rfind('(')
            end = expression.find(')', start)
            if end == -1:
                raise ValueError("Mismatched parentheses")
            sub_result = evaluate_subexpression(expression[start+1:end])
            expression = expression[:start] + str(sub_result) + expression[end+1:]

        return evaluate_subexpression(expression)

    return evaluate(expression)
