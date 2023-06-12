#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = None

    if length:
        first = sentence[0]

    return (length, first)
