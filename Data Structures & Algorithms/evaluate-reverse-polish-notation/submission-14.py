class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in {"-", "+", "*", "/"}:
                token = int(tokens[i])
                stack.append(token)
            
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                r = stack.pop()
                l = stack.pop() 
                stack.append(l-r)
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                r = stack.pop()
                l = stack.pop() 
                stack.append(int(l/r))
        return int(stack[0])