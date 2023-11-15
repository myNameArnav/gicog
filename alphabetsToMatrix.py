"""
Script: Matrix Transposer and Clipboard Copier

Description:
This script takes tab-spaced input values, converts them into a 2D array,
transposes the array, and then copies the transposed array in a Python-
friendly format to the clipboard. It runs in a loop, allowing multiple
transpositions and clipboard copies.

Functions:
- parseInput(inputStr): Parses tab-spaced input values into a 2D array.
- transposeMatrix(matrix): Transposes a given matrix (2D array).
"""

import pyperclip


def parseInput(inputStr):
    """
    Parse tab-spaced input values into a 2D array.

    Args:
    inputStr (str): The input string containing tab-spaced values.

    Returns:
    list: A 2D array containing the parsed values.
    """
    rows = inputStr.strip().split("\n")
    array2D = []

    for row in rows:
        values = row.split("\t")
        intValues = [int(val) for val in values]
        array2D.append(intValues)

    return array2D


def transposeMatrix(matrix):
    """
    Transpose a given matrix (2D array).

    Args:
    matrix (list): The input 2D array to be transposed.

    Returns:
    list: The transposed 2D array.
    """
    numRows = len(matrix)
    numCols = len(matrix[0])
    transposed = [[matrix[j][i] for j in range(numRows)] for i in range(numCols)]
    return transposed


while True:
    print("Enter tab-spaced values (press Enter twice to finish):")
    inputStr = ""
    while True:
        line = input()
        if not line:
            break
        inputStr += line + "\n"

    if not inputStr.strip():
        print("Exiting the program.")
        break

    array2D = parseInput(inputStr)
    transposedArray = transposeMatrix(array2D)

    # Generate the transposed array in a format that can be copied into Python code
    outputStr = "[\n"
    for row in transposedArray:
        outputStr += f"[{', '.join(map(str, row))}],\n"
    outputStr += "]"

    # Copy the output to the clipboard
    pyperclip.copy(outputStr)
    print("Transposed array copied to clipboard.")

# Script written by ChatGPT
