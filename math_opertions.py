import numpy as np

def add(a, b):
    "This function adds two numbers"
    return a + b


def subtract(a, b):
    "This function subtracts two numbers then prints the result which I have added"
    return a - b


def multiply(a, b):
    "This function multiplies two numbers"
    return a * b


def divide(a, b):
    "This function divides two numbers"
    return a / b


print(add(2, 3))

def mean(numbers):
    return np.mean(numbers)

numbers = [1, 2, 3, 4, 5]
print(mean(numbers))