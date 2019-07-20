#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jan Arends
"""
import random
import geopy.distance
from matplotlib import pyplot as plt


def plot_cost_function(cost_list, iter_list, log_name):
    """ Function to plot the no. of iterations
    (x-axis) vs cost (y-axis). X-axis of the plot
    contains xticks from 0 to 10000 in steps of 2000.
    matplotlib.pyplot has been user therefore.

    Parameters
    ----------
    cost_list : list
        list of the costs

    iter_list : list
        corresponding number of iterations
    """

    plt.plot(iter_list, cost_list)
    plt.savefig("./results/plots/diagram-{}.png".format(log_name))


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any cities. The first and last city remain unchanged
    since the traveller starts and ends in the same city.

    Parameters
    ----------
    curr_seq : list
        A sequence of cities, aka a route.

    Returns
    -------
    list
        Another randomly chosen possible route
    """

    random_seq = random.sample(curr_seq[:-1], len(curr_seq[:-1]))
    start_city_idx = random_seq.index(curr_seq[0])
    random_seq[0], random_seq[start_city_idx] = random_seq[start_city_idx], random_seq[0]
    random_seq.append(curr_seq[0])

    return random_seq


def get_distance(city_seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.

    Parameters
    ----------
    city_seq : list
        A sequence of cities, aka a route.

    Returns
    -------
    int
        The distance for traveling the given sequence of cities.
    """
    distance = 0
    for idx, city in enumerate(city_seq[:-1]):
        next_city = city_seq[idx + 1]
        coordinate = (float(city[2]), float(city[1]))
        next_coordinate = (float(next_city[2]), float(next_city[1]))
        distance += geopy.distance.distance(coordinate, next_coordinate).km

    return int(distance)
