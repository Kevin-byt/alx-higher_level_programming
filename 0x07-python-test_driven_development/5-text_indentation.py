#!/usr/bin/python3
"""Print text with two new lines after each '.', '?', and ':'"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    line = ""
    result = ""
    c = 0

    for char in text:
        line += char
        c += 1

        if c == len(text):
            line = line.strip()
            result = result + line

        if char in characters:
            line = line.strip()
            result = result + line + '\n\n'
            line = ""

    print(result)
