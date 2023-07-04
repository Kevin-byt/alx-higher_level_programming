#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    line = ""
    result = ""

    for char in text:
        line += char
        if char in characters:
            line = line.strip()
            result = result + line + '\n\n'
            line = ""

    print(result, end="")
