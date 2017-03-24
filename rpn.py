#!/usr/bin/env python3
import sys
import readline
import operator


operators = {
	'+': operator.add,
	'-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '%': operator.mod,
}

def calculate(myarg):
        stack = list()
        for token in myarg.split():
                try:
                        token = int(token)
                        stack.append(token)
                except ValueError:
                        function = operators[token]
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        result = function(arg1, arg2)
                        stack.append(result)
               # print(stack)
        if len(stack) != 1:
                raise TypeError("Too many parameters")
        return stack.pop()

def main():
        print("type help for information, or type exit to quit")
        while True:
                user = input('rpn calc> ')
                if user == "exit":
                        print ("exiting rpn calculator")
                        sys.exit()
                elif user == "help":
                        print ("The rpn caclulator uses the form of # # operation. type operations for a list of available operations")
                elif user == "operations":
                        print("+: addition")
                        print("-: subtraction")
                        print("*: multiplication")
                        print("/: true division")
                        print("^: exponentiation")
                        print("%: modulus")
                else:
                        try:
                                result = calculate(user)
                                print("Result: ", result)
                        except:
                                print("you must input in the form of # # operation. please try again.")

if __name__ == '__main__':
        main()
