import numpy as np


def calculate_coordinate_grid(input_dimensions: tuple[int, int], corners: list[tuple[int, int]]) -> np.ndarray:
    """
    Returns the co-ordinate grid of dimensions input_dimensions with corners listed in the corners variable.

    :param input_dimensions: number of rows and columns in the grid
    :param corners: corners of the grid (can be listed in any order)
    :return: 3-dimensional NumPy array of the grid pixel co-ordinates
    """

    bottom_left, bottom_right, top_left, top_right = sorted(corners)
    x_left, x_right, y_top, y_bottom = bottom_left[0], bottom_right[0], top_left[1], bottom_left[1]
    x_num, y_num = input_dimensions

    xvec, yvec = np.linspace(x_left, x_right, x_num), np.linspace(y_top, y_bottom, y_num)

    return np.stack(np.meshgrid(xvec, yvec), axis=-1)
