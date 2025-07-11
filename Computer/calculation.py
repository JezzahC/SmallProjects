OPERATOR_PRIORITY = {"(": 6, "**": 5, "*": 4, "/": 3, "+": 2, "-": 1}
OPERATORS = {"plus": "+", "subtract": "-", "x": "*", "divided": "/", "power": "**", "mod": "%", "floor": "//", "open": "(", "close": ")"}
DIGITS = "0123456789"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    return a / b

def exponents(a, b):
    return a ** b

def floor(a, b):
    return a // b

def modulus(a, b):
    return a % b

def parenCompute(parenExpression):
    operatorFunctions = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": exponents}
    priority = 0
    operator = ""
    for element in parenExpression:
        if element in OPERATOR_PRIORITY and OPERATOR_PRIORITY[element] > priority: priority = OPERATOR_PRIORITY[element]; operator = element
    
    if operator != "(":
        operatorIndex = parenExpression.index(operator)
        num2 = parenExpression.pop(operatorIndex + 1)
        parenExpression.pop(operatorIndex)
        num1 = parenExpression.pop(operatorIndex - 1)

        parenExpression.insert(operatorIndex - 1, operatorFunctions[operator](int(num1), int(num2)))
    
    else:
        lParenIndex = parenExpression.index("(")
        rParenIndex = parenExpression.index(")")

        parenExpression = parenExpression[lParenIndex + 1:rParenIndex]
        for i in range((rParenIndex - lParenIndex) + 1):
            parenExpression.pop(lParenIndex)

        while len(parenExpression) > 1:
            parenCompute(parenExpression)
        parenExpression.insert(lParenIndex, float(parenExpression[0]))

def maths(express: list[str]) -> float:
    expression = handleOperators(express)
    while len(expression) > 1:
        operatorFunctions = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": exponents, "//": floor, "%": modulus}
        priority = 0
        operator = ""
        for element in expression:
            if element in OPERATOR_PRIORITY and OPERATOR_PRIORITY[element] > priority: priority = OPERATOR_PRIORITY[element]; operator = element


        if operator != "(":
            operatorIndex = expression.index(operator)
            num2 = expression.pop(operatorIndex + 1)
            expression.pop(operatorIndex)
            num1 = expression.pop(operatorIndex - 1)

            expression.insert(operatorIndex - 1, operatorFunctions[operator](int(num1), int(num2)))
        else:   
            lParenIndex = expression.index("(")
            rParenIndex = expression.index(")")

            parenExpression = expression[lParenIndex + 1:rParenIndex]
            for i in range((rParenIndex - lParenIndex) + 1):
                expression.pop(lParenIndex)

            while len(parenExpression) > 1:
                parenCompute(parenExpression)
            expression.insert(lParenIndex, float(parenExpression[0]))

    return float(expression[0])

def handleOperators(expression: list[str]):
    for words in ["calculate", "please", "can", "by", "to", "the", "of"]:
        if words in expression: 
            expression.remove(words)
    for words in expression:
        if words in OPERATORS:
            index = expression.index(words)
            expression.pop(index)
            expression.insert(index, OPERATORS[words])

    return expression