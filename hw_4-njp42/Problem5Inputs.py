from enum import Enum

import numpy as np

# simulation settings
POP_SIZE = 2000         # cohort population size
SIM_TIME_STEPS = 50    # length of simulation (years)


class HealthStates(Enum):   # can assign numbers to states/text to make code more readable.
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    DEATH = 3


# transition matrix
TRANS_MATRIX = [
    [95,  5,   0,   0],   # WELL
    [0,   0,  70,  30],   # STROKE
    [0,  20,  80,   0],   # POST_STROKE
    [0,   0,   0, 100]    # DEAD
    ]


def get_trans_prob_matrix(trans_matrix):
    """
    :param trans_matrix: transition matrix containing counts of transitions between states
    :return: transition probability matrix
    """

    # initialize transition probability matrix
    trans_prob_matrix = []

    # for each row in the transition matrix
    for row in trans_matrix:
        # calculate the transition probabilities
        prob_row = np.array(row)/sum(row)
        # add this row of transition probabilities to the transition probability matrix
        trans_prob_matrix.append(prob_row)

    return trans_prob_matrix
