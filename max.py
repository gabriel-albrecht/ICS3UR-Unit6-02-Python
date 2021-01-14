#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program generates random integers and identifies the largest

import random


def maximum(random_number):
    # this function identifies the largest integer in the list

    random_number.sort()
    highest = random_number[-1]

    return highest


def main():
    # this function uses a list

    random_number = []

    # process
    for loop_counter in range(0, 10):
        a_single_number = random.randint(0, 100)
        random_number.append(a_single_number)

    print("Here are 10 completely random numbers:\n")

    for loop_counter in range(0, 10):
        print("{0} ".format(random_number[loop_counter]), end="")

    # call functions
    number = maximum(random_number)

    # output
    print("\n\nThe highest number in this list is: {0}".format(number))


if __name__ == "__main__":
    main()
