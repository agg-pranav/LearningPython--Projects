# Balanced string - eg: {([])}, {} ,[()]
# Unbalanced string - eg: {{}, [(]), {{}(})
# Program checks if the entered string is Balanced or Unbalanced using Stack


class Stack():  # Creating Stack Data Structure Class

    def __init__(self):
        self.list_stack = []

    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False

    def push(self, item):
        self.list_stack.append(item)

    def pop(self):
        self.list_stack.pop()

    def peek(self):
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]

    def __repr__(self):
        return repr(self.list_stack)


s = input("Enter the string of brakets/parenthesis/curly-braces : ")

# Splitting string into characters
ch = [char for char in s]

ns = Stack()

# Checking for Balanced string
for i in ch:
    if (i == ']' and ns.peek() == '[') or (i == '}' and ns.peek() == '{') or (i == ')' and ns.peek() == '('):
        ns.pop()
        # print('pop')
        continue
    else:
        ns.push(i)
        # print("push")
        continue
if ns.is_empty():
    print("Balanced")
else:
    print("Unbalanced")
# end
