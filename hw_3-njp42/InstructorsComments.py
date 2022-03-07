# Comments provided by the instructor or the teaching assistants after grading your submission.
import numpy as np


class Game:

    def __init__(self, id, prob):

        self.id = id
        self.Prob = prob
        self.result = []

        # self.outcomes = []
        self.reward = 0
        # self.reward = 100.00
        self.probLose = 0
        self.loseList = []


    def simulate(self, events):

        rng = np.random.RandomState(seed=self.id)
        t = 0

        for t in range(0, events):
            if rng.random_sample() < self.Prob:
                result = 0      # result of tails
                self.result.append(result)
            else:
                result = 1      # result of heads
                self.result.append(result)

        for i in range(0, len(self.result)-2):
            if self.result[i] == 0:
                if self.result[i+1] == 0:
                    if self.result[i+2] == 1:
                        self.reward += 1

        self.reward = (self.reward * 100) - 250


class MultipleGames:

    def __init__(self, id, num_games, prob):

        self.id = id
        self.Prob = prob
        self.nGames = num_games

        self.outcomes = []
        self.totalReward = []
        self.exp_value = None
        # self.totalReward = 0


    def simulate(self, events):

        for i in range(self.nGames):
            outcome = Game(self.id * self.nGames + i, prob=self.Prob)
            self.outcomes.append(outcome)

        for outcome in self.outcomes:
            outcome.simulate(events)
            self.totalReward.append(outcome.reward)

            # if not (outcome.value is None):
            #     self.value.append(outcome.value)

        self.exp_value = sum(self.totalReward)/len(self.totalReward)
        return self.exp_value

    def calc_prob_loss(self):
        count = 0
        for n in self.totalReward:
            if n <= 0:
                count += 1
        return count/len(self.totalReward)

        #     return self.loseList
        # for i in self.totalReward:
        #     if self.totalReward[i] <= 0:
        #         self.lose = 1
        #         self.loseList.append(self.lose)
        #     else:
        #         self.lose = 0
        #         self.loseList.append(self.lose)




# class CohortOutcomes:
#     def __init__(self):
#
#         self.outcomes = []    # survival times
#         self.meanSurvivalTime = None   # mean survival time
#         self.nLivingPatients = None   # survival curve (sample path of number of alive patients over time)
#
#     def extract_outcomes(self, simulated_patients):
#         """ extracts outcomes of a simulated cohort
#         :param simulated_patients: (list) of patients after being simulated """
#
#         # record survival times
#         for patient in simulated_patients:
#             if patient.survivalTime is not None:
#                 self.survivalTimes.append(patient.survivalTime)
#
#         # calculate mean survival time
#         self.meanSurvivalTime = sum(self.survivalTimes)/len(self.survivalTimes)
#
#         # survival curve
#         self.nLivingPatients = PathCls.PrevalencePathBatchUpdate(
#             name='# of living patients',
#             initial_size=len(simulated_patients),
#             times_of_changes=self.survivalTimes,
#             increments=[-1]*len(self.survivalTimes)
#         )



