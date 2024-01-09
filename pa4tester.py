from stack import Stack
class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s
'''Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators


def infixToPostfix(expression):
    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output += character
            output+= ' '

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()
                output+=' '

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()
                output += ' '

            stack.append(character)

    while stack:
        output += stack.pop()
        output += ' '

    return output

if __name__ == '__main__':
    # test infix_to_postfix function
    assert infixToPostfix('(5+2)*3') == '5 2 + 3 *'
    assert infixToPostfix('5+2*3') == '5 2 3 * +'
'''

'''Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(':0, ')':0}
Operators = ['+', '-', '*', '/', '(', ')', '^']
print(Priority['^'])
op = Stack()
postfix = ''
num = ''
infix = '(5+2)*3'
for i in infix:
    print(i)
    if i.isalpha() == True or i == '.':
        num+=i
    else:
        postfix+=num
        num = ''
    if i == '(':
        op.push(i)
    if i == ')':
        while op.size()>0 and op.peek() != '(':
            postfix += op.pop()
        op.pop()
    if i in Operators:
        if op.size()>0 or Priority[i] > Priority[op.peek()]:
            op.push(i)
        else:
            while not op.size()>0 and Priority[i] <= Priority[op.peek()]:
                postfix += op.pop()
            op.push(i)
print(postfix)
'''
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}
Operators = ['+', '-', '*', '/', '(', ')', '^']


def infix_to_postfix(infix):
    op_stack = Stack()
    postfix = ''
    num = ''
    for char in infix:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                postfix += num
                postfix += ' '
                num = ''
            if char == '(':
                op_stack.push(char)
            elif char == ')':
                while not op_stack.is_empty() and op_stack.peek() != '(':
                    postfix += op_stack.pop()
                    postfix += ' '
                if not op_stack.is_empty() and op_stack.peek() == '(':
                    op_stack.pop()
            elif char in Operators:
                if op_stack.is_empty() or Priority[char] > Priority[op_stack.peek()]:
                    op_stack.push(char)
                else:
                    while not op_stack.is_empty() and Priority[char] <= Priority[op_stack.peek()]:
                        postfix += op_stack.pop()
                        postfix += ' '
                    op_stack.push(char)
    if num:
        postfix += num
        postfix += ' '
    while not op_stack.is_empty():
        postfix += op_stack.pop()
        postfix += ' '
    return postfix.strip()


if __name__ == '__main__':
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
'''
class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
class ExpTree(BinaryTree):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def postfix_to_expr_tree(postfix):
        print(postfix)
        operators = ['-','+','*', '^']
        s = Stack()
        for symbol in postfix:
            t = Node(symbol)
            if symbol in operators:
                t1= s.pop()
                t2 = s.pop()
                t.right = t1
                t.left = t2
            s.push(t)
        t=s.pop()
        return t

postfix = '5 2 3 * +'.split()
tree = ExpTree.postfix_to_expr_tree(postfix)

print(str(tree))
'''assert str(tree) == '(5+(2*3))'''