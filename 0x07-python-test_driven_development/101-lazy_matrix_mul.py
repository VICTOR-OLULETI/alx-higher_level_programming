#!/usr/bin/python3
"""
This module takes two matrices and multiply them using the numpy library
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
        Args:
            - m_a: list of lists (int or float)
            - m_b: list of lists (int or float)
    """
    return np.matmul(m_a, m_b)
