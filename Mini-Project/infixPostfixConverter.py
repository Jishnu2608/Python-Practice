import tkinter as tk
import re


# Function to convert infix to postfix
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


# Function to convert infix to prefix
def infix_to_prefix(expression):
    reversed_expression = expression[::-1]
    reversed_expression = re.sub(r'\(', 'temp', reversed_expression)
    reversed_expression = re.sub(r'\)', '(', reversed_expression)
    reversed_expression = re.sub(r'temp', ')', reversed_expression)
    postfix = infix_to_postfix(reversed_expression)
    return postfix[::-1]

def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            infix = f'({operand1}{char}{operand2})'
            stack.append(infix)
    return stack[0]