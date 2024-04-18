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
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    function_list = [add, subtract, multiply, divide]
    random = randint(0, 4)
    answer = function_list[random](num1, num2)

    # list[num1, num2, answer, start, end]
    # for index in range()
    return [num1, num2, answer, ]

