#!/usr/bin/python3
"""compulsory line"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    previous = ""
    for char in text:
        # leading whitespace
        if char == " " and char == text[0] and previous == "":
            previous = "\n"
            continue
        # whitespaces after newline
        if char == " " and previous == "\n":
            continue
        # matching character, print char, print newlines
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            previous = "\n"
        else:
            print(char, end="")
            previous = char
