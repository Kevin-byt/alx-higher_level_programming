#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if (not isinstance(m_a, list)):
        raise TypeError("m_a must be a list")

    if (not isinstance(m_b, list)):
        raise TypeError("m_b must be a list")

    if (not all(isinstance(row, list) for row in m_a)):
        raise TypeError("m_a must be a list of lists")

    if (not all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_b must be a list of lists")

    def is_empty(matrix):
        return all(not item for item in matrix)

    if (is_empty(m_a)):
        raise ValueError("m_a can't be empty")

    if (is_empty(m_b)):
        raise ValueError("m_b can't be empty")

    if (not all(isinstance(element, (int, float))
                for element in [element for row in m_a for element in row])):
        raise TypeError("m_a should contain only integers or floats")

    if (not all(isinstance(element, (int, float))
                for element in [element for row in m_b for element in row])):
        raise TypeError("m_b should contain only integers or floats")

    if (not all(len(row) == len(m_a[0]) for row in m_a)):
        raise TypeError("each row of m_a must be of the same size")

    if (not all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("each row of m_b must be of the same size")

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    # Create an empty result matrix
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return (result)
