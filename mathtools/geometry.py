# mathtools/geometry.py

import math
from typing import Tuple, List

def calculate_circle_properties(radius: float) -> Tuple[float, float]:
    """
    Calculate the area and circumference of a circle.

    Parameters
    ----------
    radius : float
        The radius of the circle

    Returns
    -------
    Tuple[float, float]
        A tuple containing (area, circumference)

    Raises
    ------
    ValueError
        If radius is negative

    Examples
    --------
    >>> area, circumference = calculate_circle_properties(1.0)
    >>> print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")
    Area: 3.14, Circumference: 6.28
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


def compute_polygon_area(vertices: List[Tuple[float, float]]) -> float:
    """
    Calculate the area of a polygon using the shoelace formula.

    Parameters
    ----------
    vertices : List[Tuple[float, float]]
        List of (x, y) coordinates of the polygon vertices in order

    Returns
    -------
    float
        Area of the polygon

    Notes
    -----
    Uses the shoelace formula (also known as surveyor's formula).
    Vertices should be ordered either clockwise or counterclockwise.

    Examples
    --------
    >>> # Calculate area of a triangle
    >>> vertices = [(0, 0), (1, 0), (0, 1)]
    >>> area = compute_polygon_area(vertices)
    >>> print(f"Area: {area:.2f}")
    Area: 0.50
    """
    n = len(vertices)
    area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
        
    return abs(area) / 2.0