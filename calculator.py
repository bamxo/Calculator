# author: Landon Nguyen
# date: March 3, 2023
# file: calculator.py a Python file that defines a calculator
# input: data types are stored in a list
# output: stored data types can only be added, removed, and peeked at from the top of the stack

from tree import ExpTree

def infix_to_postfix(infix):
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix = []
    num = ''
    for char in infix:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                postfix.append(num)
                num = ''
            if char in precedence:
                while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
    if num:
        postfix.append(num)
    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)


def calculate(infix):
    postfix = infix_to_postfix(infix)
    tree = ExpTree.make_tree(postfix.split())
    return ExpTree.evaluate(tree)


# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    

    print('Welcome to Calculator Program!')
    while True:
        infix = input(f'Please enter your expression here. To quit enter \'quit\' or \'q\':\n')
        if infix == 'quit' or infix == 'q':
            print('Goodbye!')
            break
        else:
            print(calculate(infix))
