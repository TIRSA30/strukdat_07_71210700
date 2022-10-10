class PrefixConverter:
    def __init__(self):
        self.stackList = []
    
    def __len__(self):
        return len(self.stackList)

    def is_empty(self): #jika di len kosong maka true, untuk mengecek ksong atau tidak
        return len(self.stackList) == 0

    # method untuk menambahkan data baru 
    def push(self,data):
        self.stackList.append(data)

    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    # method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    
    def isOperator(c):
        return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))

    def getPriority(C):
        if (C == '-' or C == '+'):
            return 1
        elif (C == '*' or C == '/'):
            return 2
        elif (C == '^'):
            return 3
        return 0

    def cekValidExpression(self, expression):
        if "(" and ")" in expression:
            return "Expresi Infix yang anda masukkan tidak valid !!"
        else:
            return True

    def infixToPrefix(self,expression):
        operators = []

        operands = []

        for i in range(len(expression)):

            if (expression[i] == '('):
                operators.append(expression[i])


            elif (expression[i] == ')'):
                while (len(operators)!=0 and operators[-1] != '('):
                    # operand 1
                    op1 = operands[-1]
                    operands.pop()

                    # operand 2
                    op2 = operands[-1]
                    operands.pop()

                    # operator
                    op = operators[-1]
                    operators.pop()

                    tmp = op + op2 + op1
                    operands.append(tmp)

                operators.pop()

            elif (not isOperator(expression[i])):
                operands.append(expression[i] + "")

            else:
                while (len(operators)!=0 and getPriority(expression[i]) <= getPriority(operators[-1])):
                    op1 = operands[-1]
                    operands.pop()

                    op2 = operands[-1]
                    operands.pop()

                    op = operators[-1]
                    operators.pop()

                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.append(expression[i])

        while (len(operators)!=0):
            op1 = operands[-1]
            operands.pop()

            op2 = operands[-1]
            operands.pop()

            op = operators[-1]
            operators.pop()

            tmp = op + op2 + op1
            operands.append(tmp)

        return operands[-1]


if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))

