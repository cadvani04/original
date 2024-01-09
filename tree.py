# author: Curran Advani
# date: Mar 16, 2023
# file: tree.py
# input: postfix expression
# output: making and evaluating an expression tree for a calculator
from stack import Stack


class BinaryTree: #From Lab #7
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


'''class ExpTree(BinaryTree):
    def make_tree(postfix):
        print(postfix)
        operators = ['-', '+', '*', '^']
        s = Stack()
        for symbol in postfix:
            s.push(ExpTree(symbol))
            if symbol in operators:
                temp = ExpTree(symbol)
                temp.rightChild = s.pop()
                temp.leftChild = s.pop()
                s.push(temp)
        return ExpTree()'''


class ExpTree(BinaryTree):
    def __init__(self, value): #super init for binary tree
        super().__init__(value)



    def make_tree(postfix):
        operators = ['-', '+', '*', '^', '/']
        s = Stack()
        for symbol in postfix:
            if symbol not in operators:
                s.push(ExpTree(symbol))
            else:
                temp = ExpTree(symbol)
                temp.rightChild = s.pop()
                temp.leftChild = s.pop()
                s.push(temp)
        return s.pop()

    def preorder(tree):
        s = ''
        if tree != None:
            if type(tree) != str:
                s = tree.getRootVal()
                s += ExpTree.preorder(tree.getLeftChild())
                s += ExpTree.preorder(tree.getRightChild())
            else:
                s+=(tree)
        return s

    def inorder(tree):
        if tree.getRightChild()==None:
            tree.rightChild = ''
        if tree.getLeftChild()==None:
            tree.leftChild=''
        if tree.getLeftChild()=='' and tree.getRightChild() == '':
            return str(tree.getRootVal())
        return '(' + str(tree.getLeftChild()) + str(tree.getRootVal()) + str(tree.getRightChild()) + ')'


    def postorder(tree):
        if tree != None:
            s=''
            if type(tree) != str:
                s = ExpTree.postorder(tree.getLeftChild())
                s += ExpTree.postorder(tree.getRightChild())
                s += str(tree.getRootVal())
            else:
                s+=tree
            return s
        else:
            return ''

    def evaluate(tree):
        if tree is None: #if none
            return 0
        rootval = tree.getRootVal() #get rootval to evaluate
        if rootval not in ['+', '-', '*', '/', '^']:
            return float(rootval) #float bc what if 1.00
        leftsum = ExpTree.evaluate(tree.getLeftChild()) #recursively calling getting the root values
        rightsum = ExpTree.evaluate(tree.getRightChild())
        if rootval == '+':
            return leftsum + rightsum
        if rootval == '-':
            return leftsum - rightsum
        if rootval == '/':
            return leftsum / rightsum
        if rootval == '*':
            return leftsum * rightsum
        if rootval == '^':
            return leftsum ** rightsum



    def __str__(self):
        return ExpTree.inorder(self)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
