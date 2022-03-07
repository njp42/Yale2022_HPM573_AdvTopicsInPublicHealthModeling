from enum import Enum
import numpy as np
import SimPy.Markov as Markov

# simulation settings
POP_SIZE = 2000         # cohort population size
SIMULATION_LENGTH = 50    # length of simulation (years)
# annual probability of background mortality among adults
# (number per year per 100,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 4103.8 / 100000


class HealthStates(Enum):
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STROKE_DEATH = 3
    NATUAL_DEATH = 4


# Problem 1
# Part 1
# print(41.4*100 - 36.2, "per 100,000")
L0 = -np.math.log(1-(4103.8/100000))
# print("Annual rate of non-Stroke mortality: ", L0)   # Lambda 0

# Part 2
# print("Annual rate of first Stroke: ", -np.math.log(1-(15/1000)))

# Part 3
L1 = 0.75 * -np.math.log(1-(15/1000))
L2 = 0.25 * -np.math.log(1-(15/1000))
# print("Annual rate of Well to Stroke = ", L1)  # Lambda 1
# print("Annual rate of Well to Stroke Death = ", L2)   # Lamda 2

# Part 4
# print("Annual rate of recurrent stroke events = ", (-1/5) *np.math.log(1-(17/100)))

# Part 5
L3 = 0.70 * (-1/5)*np.math.log(1-(17/100))
L4 = 0.3 * (-1/5)*np.math.log(1-(17/100))
# print("Annual rate of recurrent stroke to Stroke = ", L3)    # Lambda 3
# print("Annual rate of recurrent stroke to Stroke Death = ", L4)   # Lambda 4

# Part 6
L5 = 52
# print("Annual rate of Stroke to Post Stroke = ", L5)  # Lambda 5

# Without Anticoagulation
trans_rate_matrix = [
    [None,     L1,    0,    L2,   L0],   # WELL
    [0,      None,   L5,     0,    0],   # STROKE
    [0,     L3,    None,    L4,   L0],   # POST-STROKE
    [0,     0,      0,    None,    0],   # STROKE DEATH
    [0,     0,      0,    0,    None]    # NON-STROKE DEATH
    ]


# Problem 2
L3b = 0.55 * (0.70 * (-1/5)*np.math.log(1-(17/100)))    # new Lambda 3
L4b = 0.55 * (0.3 * (-1/5)*np.math.log(1-(17/100)))      # new Lambda 4
L0b = 1.05 * -np.math.log(1-(4103.8/100000))            # new Lambda 0

# Under Anticoagulation
trans_rate_matrix2 = [
    [None,     L1,    0,    L2,      L0],   # WELL
    [0,      None,   L5,     0,       0],   # STROKE
    [0,     L3b,    None,    L4b,   L0b],   # POST-STROKE  L4 * .55?
    [0,     0,      0,    None,       0],   # STROKE DEATH
    [0,     0,      0,    0,       None]    # NON-STROKE DEATH
    ]

