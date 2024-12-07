def Operator(S):
    return S[0]


def Operand1(S):
    return S[1]


def Operand2(S):
    return S[2]


def IsEmpty(S):
    return S == []


def EvaluateExpression(S):
    if IsEmpty(S):
        return []
    elif Operator(S) == "+":
        return Operand1(S) + Operand2(S)
    elif Operator(S) == "-":
        return Operand1(S) - Operand2(S)
    elif Operator(S) == "*":
        return Operand1(S) * Operand2(S)
    elif Operator(S) == "/":
        return Operand1(S) / Operand2(S)


print(EvaluateExpression(["+", 3, 5]))
print(EvaluateExpression(["-", 10, 4]))
