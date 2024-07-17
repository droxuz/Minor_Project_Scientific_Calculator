import operator
import re
class BasicArithmetic:

    def addition(self, num1, num2):
        sum= num1 + num2
        return sum
    
    def subtraction(self, num1, num2):
        difference = num1 - num2
        return difference
    
    def multiplication(self, num1, num2):
        product = num1 * num2
        return product
    
    def division(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot Divide by Zero. ")
        quotient = num1 / num2
        return quotient
    
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {e}"

