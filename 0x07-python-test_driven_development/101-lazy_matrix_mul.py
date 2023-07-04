#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    if (not isinstance(m_a, list)):
        raise TypeError("Ensure that m_a is a list")

    if (not isinstance(m_b, list)):
        raise TypeError("Ensure that m_b is a list")

    if (not all(isinstance(row, list) for row in m_a)):
        raise TypeError("Ensure that m_a is a list of lists")

    if (not all(isinstance(row, list) for row in m_b)):
        raise TypeError("Ensure that m_b is a list of lists")

    def is_empty(matrix):
        return all(not item for item in matrix)

    if (is_empty(m_a)):
        raise ValueError("Ensure that m_a is not empty")

    if (is_empty(m_b)):
        raise ValueError("Ensure that m_b is not empty")

    if (not all(isinstance(element, (int, float))
                for element in [element for row in m_a for element in row])):
        raise TypeError("Ensure that m_a contains only integers or floats")

    if (not all(isinstance(element, (int, float))
                for element in [element for row in m_b for element in row])):
        raise TypeError("Ensure that m_b contains only integers or floats")

    if (not all(len(row) == len(m_a[0]) for row in m_a)):
        raise TypeError("all rows of m_a must be equal in size")

    if (not all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("all rows of m_b must be equal in size")

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b are misaligned, can't be multiplied")

    result = np.matmul(m_a, m_b)

    return (result)
