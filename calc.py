class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def doMath2(op, op1, op2):
        if op == "^":
            return op1 ** op2
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

    def doMath(op, op1):
        if op == "~":
            return op1 * -1

    def infixToPostfix(self, infixexpr):
        prec = {}
        prec["^"] = 4
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        prec["~"] = 2
        opStack = Stack()
        postfixList = []
        tokenList = infixexpr.split()

        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(' :
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)

    def postfixEval(self, postfixExpr):
        operandStack = Stack()

        tokenList = postfixExpr.split()

        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            elif token == "~":
                operand1 = operandStack.pop()
                result = Stack.doMath(token, operand1)
                operandStack.push(result)
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = Stack.doMath2(token,operand1,operand2)
                operandStack.push(result)

        return operandStack.pop()



#a = infixToPostfix(input_buffer)
#print(a)

#value = postfixEval(a)
#print("The final result is:  " + str(value))
if __name__ == '__main__':
    calc = Stack()
    while True:
        try:
            input_buffer = input("> ")
            if input_buffer.lower() == "exit":
                break
            a = calc.infixToPostfix(input_buffer)
            print(a)
            value = calc.postfixEval(a)
            print("The final result is:  " + str(value))
        except EOFError:
            break