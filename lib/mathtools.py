from math import hypot
from operator import add, sub
from lib.constants import *

def euclidean(p1, p2):
    return hypot(p1[X] - p2[X], p1[Y]- p2[Y])

def manhattan(p1, p2):
    return abs(p1[X] - p2[X]) + abs(p1[Y] - p2[Y])

def list_add(p1, p2):
    return tuple(map(add, p1, p2))

def list_sub(p1, p2):
    return tuple(map(sub, p1, p2))

def list_mul(p1, p2):
    return tuple(map(lambda x, y: x*y, p1, p2))