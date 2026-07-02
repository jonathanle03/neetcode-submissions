class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                stack.append(operand_1 + operand_2)
            elif token == "-":
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                stack.append(operand_1 - operand_2)
            elif token == "*":
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                stack.append(operand_1 * operand_2)
            elif token == "/":
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                stack.append(operand_1 / operand_2)
            else:
                stack.append(int(token))
        
        return int(stack[0])