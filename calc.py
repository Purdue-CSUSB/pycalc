#!/usr/bin/env python

# Copyright 2016 -- Levi Starrett & Jay Hankins
# for educational purposes only
#
# For use in CS 190: https://github.com/Purdue-CSUSB/CS-190-F2016/
#
# Calculator -- a four function calculator commandline tool

import sys

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# num1 -- addend
# num2 -- augend
def add(num1, num2):
    return num1 + num2

# Subtract function
# a -- minuend
# b -- subtrahend
def sub(num1, num2):
    return num1 - num2

# Multiply function
# num1 -- multiplicand
# num2 -- multiplier
def mult(num1, num2):
    return num1 * num2

# Divide function
# num1 -- dividend
# num2 -- divisor
def div(num1, num2):
    return num1 / num2


# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

num1 = None
num2 = None
op = None

while (True):
    # get input values
    num1 = raw_input("Enter the first argument: ")
    op = raw_input("Enter the operation: ")
    num1 = raw_input("Enter the second argument: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print "Invalid number argument..."
        op = None

    # decide function
    if (op != None):
        if (op == "+"):
            print "Sum: ", add(num1, num2)
        elif (op == "-"):
            print "Difference: ", sub(num1, num2)
        elif (op == "*"):
            print "Product: ", mult(num1, num2)
        elif (op == "/"):
            print "Quotient: ", div(num1, num2)
        else:
            print "Invalid operation..."

    q = raw_input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #
