# author: Curran Advani
# date: Mar 16, 2023
# file: calculator.py
# input: math expressions
# output: the answer to math expressions
from stack import Stack
from tree import ExpTree

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}
Operators = ['+', '-', '*', '/', '(', ')', '^']

def infix_to_postfix(infix): #going from what we see to what the computer sees
    op_stack = Stack() # making stack for the types of operators
    postfix = ''
    num = ''
    for char in infix:
        if char.isdigit() or char == '.': # if its a digit add it to num
            num += char
        else:
            if num: #keep adding nums to postfix
                postfix += num
                postfix += ' '
                num = ''
            if char == '(':
                op_stack.push(char)
            elif char == ')': #keep popping operating within parentheses into postfix until get to start of brackets
                while not op_stack.is_empty() and op_stack.peek() != '(':
                    postfix += op_stack.pop()
                    postfix += ' '
                if not op_stack.is_empty() and op_stack.peek() == '(':
                        op_stack.pop()
            elif char in Operators: #characters are in priority
                if op_stack.is_empty() or Priority[char] > Priority[op_stack.peek()]:
                    op_stack.push(char)
                else:
                    while not op_stack.is_empty() and Priority[char] <= Priority[op_stack.peek()]:
                        postfix += op_stack.pop()
                        postfix += ' '
                    op_stack.push(char)
    if num: #if the num still exists then add it to postfix
        postfix += num
        postfix += ' '
    while not op_stack.is_empty(): #op_stack is emptied putting all operators in postfix
        postfix += op_stack.pop()
        postfix += ' '
    return postfix.strip()

    #write to expression tree


def calculate(infix):
    postfix = infix_to_postfix(infix) # write to infixtopostfix
    postfix = postfix.split()
    tree = ExpTree.make_tree(postfix) # write to expression tree
    return ExpTree.evaluate(tree)

    # write to expression tree


# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    print('Welcome to Calculator Program!')
    k=True
    while k: #main calculator function
        print("Please enter your expression here. To quit enter 'quit' or 'q':")
        q = str(input())
        if q == 'q' or q=='quit':
            k=False
        else:
            print(calculate(q))


