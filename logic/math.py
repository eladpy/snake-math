from Constants import *
import pygame
from random import randint


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def math():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    function_list = [add, subtract, multiply, divide]
    random = randint(0, 3)
    answer = function_list[random](num1, num2)
    bottom_range = answer - 10
    top_range = answer + 10
    return [num1, num2, answer, bottom_range, top_range, function_list[random]]


def to_string(num1, num2, operator):
    if operator == add:
        operator = "+"
    elif operator == subtract:
        operator = "-"
    elif operator == multiply:
        operator = "*"
    else:
        operator = "/"
    return f'{num1} {operator} {num2} = ?'
