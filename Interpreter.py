import sys

__author__ = 'Hrafnkell'

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Interpreter(object):
    ''' Reads stack-based intermediate code from standard input
        and interprets it on the fly'''

    def __init__(self):
        self.stack = Stack()
        self.map = {}
        self.input_line = []

    def fetch(self):
        input_string = input()
        self.input_line = input_string.split()

    def decode(self):
        # variables for easy calling
        if self.input_line == []:
            return
        command = self.input_line[0]
        if command == "PUSH":
            operator = self.input_line[1]
        stack = self.stack
        map = self.map

        if command == "PUSH":
            if operator in map:
                val = map[operator]
                stack.push(val)
            else:
                stack.push(operator)
        elif command == "ADD":
            if not stack.is_empty():
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                stack.push(v1 + v2)
        elif command == "SUB":
            if not stack.is_empty():
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                stack.push(v2 - v1)
        elif command == "MULT":
            if not stack.is_empty():
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                stack.push(v1 * v2)
        elif command == "ASSIGN":
            if not stack.is_empty():
               value = int(stack.pop())
               key = stack.pop()
               map[key] = value

        elif command == "PRINT":
            if not stack.is_empty():
               print(stack.pop())
               sys.exit(1)
        else:
            print("Error of operator: %s" % (command))
            sys.exit(1)


myInterpreter = Interpreter()

while True:
    myInterpreter.fetch()
    myInterpreter.decode()

