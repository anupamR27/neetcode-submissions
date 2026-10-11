class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+' :
                stack.append(stack.pop() + stack.pop())

            elif c == '-' :
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)

            elif c == '*' :
                stack.append(stack.pop() * stack.pop())

            elif c == '/' :
                a, b = stack.pop() , stack.pop()
                d = (int(b/a))
                stack.append(d)

            else:
                stack.append(int(c))

        return stack[0]