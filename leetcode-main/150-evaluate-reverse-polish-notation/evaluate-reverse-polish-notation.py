class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for string in tokens:
            if string not in "+-/*":
                stack.append(string)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if string == '+':
                    stack.append(str(num1 + num2))
                elif string == '-':
                    stack.append(str(num1 -num2))
                elif string == '*':
                    stack.append(str(num1 * num2))
                elif string == '/':
                    stack.append(str(int(num1 / num2)))
        return int(stack[-1])

                