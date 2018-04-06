"""
Tests specific to the collections module.
"""
from __future__ import absolute_import, division, print_function

import io

import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal
import pytest

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.testing.decorators import image_comparison


def generate_linear_gradient():
    '''
    array comparison of a gradient list to make sure all values are between
    the start and finish at equal intervals.
    '''
    cstart = '0'
    cend = '1'
    n = 5
    res_gradient = [(0,0,0,1), (0.25,0.25,0.25,1), (0.5,0.5,0.5,1), (0.75,0.75,0.75,1), (1,1,1,1)]
    np.testing.assert_equal(mcolors.linear_gradient(cstart, cend, n), res_gradient)

@image_comparison(baseline_images=['bullet'], extensions=['png'], style='mpl20')
def test_bullet_graph():
    x = [6]
    ranges = [[0, 2, 4, 6, 8]]
    fig, ax = plt.subplots()
    ax.bullet(x, ranges)

@image_comparison(baseline_images=['bullet_uniform_range'], extensions=['png'], style='mpl20')
def test_bullet_graph_uniform_range():
    x = [6, 8, 10]
    ranges = [[0, 2, 4, 6, 8, 10, 12, 14, 16]]
    fig, ax = plt.subplots()
    ax.bullet(x, ranges)

@image_comparison(baseline_images=['bullet_all_distinct_range'], extensions=['png'], style='mpl20')
def test_bullet_graph_uniform_range():
    x = [6, 8, 10]
    ranges = [[0, 2, 4, 6, 8, 10, 12, 14, 16], [0, 4, 12, 16], [0, 8, 16]]
    fig, ax = plt.subplots()
    ax.bullet(x, ranges)

@image_comparison(baseline_images=['bullet_target'], extensions=['png'], style='mpl20')
def test_bullet_graph_target():
    x = [6, 8, 10]
    ranges = [[0, 2, 4, 6, 8, 10, 12, 14, 16]]
    tar = [4, 12, 10]
    fig, ax = plt.subplots()
    ax.bullet(x, ranges, targets=tar, targetcolor="b")

@image_comparison(baseline_images=['color_bullet'], extensions=['png'], style='mpl20')
def test_colored_bullet_graph():
    x = [6, 8, 10]
    ranges = [[0, 2, 4, 6, 8, 10, 12, 14, 16]]
    tar = [4, 12, 10]
    fig, ax = plt.subplots()
    ax.bullet(x, ranges, targets=tar, targetcolor="b", startcolor="r", endcolor="y")

def test_bullet_bad_inputs():
    fig, ax = plt.subplots()
    x = ['egg']
    ranges = [[0, 1]]
    with pytest.raises(ValueError):
        ax.bullet(x, ranges);

def test_bullet_negative_data_values():
    '''
    '''
    fig, ax = plt.subplots()
    x = [-1]
    ranges = [[0, 1, 2]]
    with pytest.raises(ValueError):
        ax.bullet(x, ranges);

def test_bullet_ambiguous_ranges():
    fig, ax = plt.subplots()
    x = [1, 2, 3]
    ranges = [[0, 1], [2, 4]]
    with pytest.raises(ValueError):
        ax.bullet(x, ranges);