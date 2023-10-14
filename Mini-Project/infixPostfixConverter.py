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

def prefix_to_infix(expression):
    stack = []
    for char in expression[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = f'({operand1}{char}{operand2})'
            stack.append(infix)
    return stack[0]

def convert():
    input_text = input_entry.get()
    output_text.delete(1.0, tk.END)

    if conversion_type.get() == "Infix to Postfix":
        result = infix_to_postfix(input_text)
    elif conversion_type.get() == "Infix to Prefix":
        result = infix_to_prefix(input_text)
    elif conversion_type.get() == "Postfix to Infix":
        result = postfix_to_infix(input_text)
    elif conversion_type.get() == "Prefix to Infix":
        result = prefix_to_infix(input_text)

    output_text.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Expression Converter")

# Create and configure widgets
input_label = tk.Label(window, text="Enter Expression:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

conversion_type = tk.StringVar()
conversion_type.set("Infix to Postfix")

radio_frame = tk.Frame(window)
radio_frame.pack()


infix_to_postfix_radio = tk.Radiobutton(radio_frame, text="Infix to Postfix", variable=conversion_type, value="Infix to Postfix")
infix_to_postfix_radio.pack(side=tk.LEFT)


infix_to_prefix_radio = tk.Radiobutton(radio_frame, text="Infix to Prefix", variable=conversion_type, value="Infix to Prefix")
infix_to_prefix_radio.pack(side=tk.LEFT)


postfix_to_infix_radio = tk.Radiobutton(radio_frame, text="Postfix to Infix", variable=conversion_type, value="Postfix to Infix")
postfix_to_infix_radio.pack(side=tk.LEFT)


prefix_to_infix_radio = tk.Radiobutton(radio_frame, text="Prefix to Infix", variable=conversion_type, value="Prefix to Infix")
prefix_to_infix_radio.pack(side=tk.LEFT)

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

output_label = tk.Label(window, text="Result:")
output_label.pack()
output_text = tk.Text(window, height=5, width=40)
output_text.pack()

# Run the application
window.mainloop()
