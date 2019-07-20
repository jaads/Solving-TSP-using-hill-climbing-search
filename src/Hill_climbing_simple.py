#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jan Arends
"""

import argparse
import random
import timeit
import logging
import os
from helper import *


def hill_climb_simple(start_seq, log_name):
    """Implementation of simple hill climbing algorithm
    for the travelling salesman problem.
    The hill climbing algorithm runs 10,000 iterations and
    restarts at every 2,000 iterations with a randomly chosen route.

    Parameters
    ----------
    start_seq : list
        A sequence of city which represent a initial route.

    Returns
    -------
    (int, list)
        The result of the algorithm. In fact number of kilometers
        for the best sequence found along with the corresponding sequence.
    """

    start_seq.append(start_seq[0])
    curr_seq = start_seq
    curr_dist = get_distance(curr_seq)
    best_dist = curr_dist
    overall_best_dist = best_dist
    best_seq = curr_seq
    overall_best_seq = best_seq
    costs_list = []
    iter_nr_list = []

    logging.info("Starting hill climbing algorithm for {} cities".format(len(start_seq) - 1))
    logging.info("Start distance: {}".format(curr_dist))

    for x in range(1, 10000):

        if x % 2000 == 0:
            best_seq = start_seq
            best_dist = get_distance(start_seq)
            logging.info("New round after {} iterations".format(x))

        curr_seq = get_successors(curr_seq)
        curr_dist = get_distance(curr_seq)

        costs_list.append(best_dist)
        iter_nr_list.append(x)

        if curr_dist < best_dist:
            best_seq = curr_seq
            best_dist = get_distance(best_seq)
            if curr_dist < overall_best_dist:
                overall_best_seq = best_seq
                overall_best_dist = best_dist
            logging.info("New best: {} km - found after {} iterations".format(best_dist, x))

    plot_cost_function(costs_list, iter_nr_list, log_name)
    return overall_best_dist, overall_best_seq


if __name__ == '__main__':
    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    # Configure logging
    log_name = (args.filename).replace("data/", "")
    logging.basicConfig(filename='./results/log-{}'.format(log_name),
                        level=logging.INFO,
                        format='%(asctime)s\t\t%(message)s',
                        filemode='w')

    # Getting the list of cities and their coordinates
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]

    # Generating a random initial sequence
    number_of_cities = len(city_names)
    random_start_seq = random.sample(list_of_cities[1:], number_of_cities)

    # Calculating the least distance using simple hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_simple(random_start_seq, log_name)
    end_time = timeit.default_timer()

    logging.info("Results from Simple hill climbing:")
    logging.info("Best Sequence: {}".format(best_seq))
    logging.info("Least distance is {} km".format(least_distance))
    logging.info("Time: {}".format(end_time - start_time))
