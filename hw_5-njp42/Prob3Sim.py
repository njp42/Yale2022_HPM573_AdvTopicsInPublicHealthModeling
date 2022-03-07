import numpy as np

import SimPy.Markov as Markov
import SimPy.SamplePath as Path
from InputData import HealthStates


class Patient:
    def __init__(self, id, trans_rate_matrix):
        """ initiates a patient
        :param id: ID of the patient
        :param trans_rate_matrix: transition rate matrix
        """
        self.id = id
        self.transRateMatrix = trans_rate_matrix
        self.stateMonitor = PatientStateMonitor()  # patient state monitor

    def simulate(self, sim_length):
        """ simulate the patient over the specified simulation length """

        # random number generator for this patient
        rng = np.random.RandomState(seed=self.id)
        # gillespie algorithm
        gillespie = Markov.Gillespie(transition_rate_matrix=self.transRateMatrix)

        t = 0  # simulation time
        if_stop = False

        while not if_stop:
            # find time until next event (dt), and next state
            # (note that the gillespie algorithm returns None for dt if the process
            # is in an absorbing state)
            dt, new_state_index = gillespie.get_next_state(
                current_state_index=self.stateMonitor.currentState.value,
                rng=rng)

            # stop if time to next event (dt) is None (i.e. we have reached an absorbing state)
            if dt is None:
                if_stop = True

            else:
                # else if next event occurs beyond simulation length
                if dt + t > sim_length:
                    # advance time to the end of the simulation and stop
                    t = sim_length
                    # the individual stays in the current state until the end of the simulation
                    new_state_index = self.stateMonitor.currentState.value
                    if_stop = True
                else:
                    # advance time to the time of next event
                    t += dt
                # update health state
                self.stateMonitor.update(time=t, new_state=HealthStates(new_state_index))


class PatientStateMonitor:
    """ to update patient outcomes (years survived, cost, etc.) throughout the simulation """
    def __init__(self):

        self.currentState = HealthStates.WELL       # current health state
        # self.temporaryState = HealthStates.STROKE   # temporary stroke state
        self.strokeNumber = 0                       # number of strokes
        self.survivalTime = None                    # survival time
        self.timeToPostStroke = None                # time to develop AIDS

    def update(self, time, new_state):
        """
        update the current health state to the new health state
        :param time: current time
        :param new_state: new state
        """

        if new_state == HealthStates.STROKE or new_state ==HealthStates.STROKE_DEATH:
            self.strokeNumber += 1

        # update survival time
        if new_state in (HealthStates.STROKE_DEATH, HealthStates.NATUAL_DEATH):
            self.survivalTime = time

        # update time until AIDS
        if self.currentState != HealthStates.POST_STROKE and new_state == HealthStates.POST_STROKE:
            self.timeToPostStroke = time

        # update current health state
        self.currentState = new_state


class Cohort:
    def __init__(self, id, pop_size, trans_rate_matrix):
        """ create a cohort of patients
        :param id: cohort ID
        :param pop_size: population size of this cohort
        :param trans_rate_matrix: transition rate matrix
        """
        self.id = id
        self.popSize = pop_size
        self.transRateMatrix = trans_rate_matrix
        self.cohortOutcomes = CohortOutcomes()  # outcomes of the this simulated cohort

    def simulate(self, sim_length):
        """ simulate the cohort of patients over the specified duration
        :param sim_length: simulation length
        """

        # populate and simulate the cohort
        for i in range(self.popSize):
            # create a new patient (use id * pop_size + n as patient id)
            patient = Patient(id=self.id * self.popSize + i,
                              trans_rate_matrix=self.transRateMatrix)
            # simulate
            patient.simulate(sim_length)

            # store outputs of this simulation
            self.cohortOutcomes.extract_outcome(simulated_patient=patient)

        # calculate cohort outcomes
        self.cohortOutcomes.calculate_cohort_outcomes(initial_pop_size=self.popSize)


class CohortOutcomes:
    def __init__(self):

        self.survivalTimes = []         # patients' survival times
        self.timesToPostStroke = []           # patients' times to Post Stroke
        self.totalNumberOfStrokes = []
        self.meanSurvivalTime = None    # mean survival times
        self.meanTimeToPostStroke = None      # mean time to AIDS
        self.nLivingPatients = None     # survival curve (sample path of number of alive patients over time)
        self.meanStrokes = None

    def extract_outcome(self, simulated_patient):
        """ extracts outcomes of a simulated patient
        :param simulated_patient: a simulated patient"""

        # record survival time and time until AIDS
        if simulated_patient.stateMonitor.survivalTime is not None:
            self.survivalTimes.append(simulated_patient.stateMonitor.survivalTime)
        if simulated_patient.stateMonitor.timeToPostStroke is not None:
            self.timesToPostStroke.append(simulated_patient.stateMonitor.timeToPostStroke)
        if simulated_patient.stateMonitor.strokeNumber is not None:
            self.totalNumberOfStrokes.append(simulated_patient.stateMonitor.strokeNumber)

    def calculate_cohort_outcomes(self, initial_pop_size):
        """ calculates the cohort outcomes
        :param initial_pop_size: initial population size
        """

        # calculate mean survival time
        self.meanSurvivalTime = sum(self.survivalTimes) / len(self.survivalTimes)
        # calculate mean time to AIDS
        self.meanTimeToPostStroke = sum(self.timesToPostStroke)/len(self.timesToPostStroke)

        self.meanStrokes = sum(self.totalNumberOfStrokes)/len(self.totalNumberOfStrokes)

        # survival curve
        self.nLivingPatients = Path.PrevalencePathBatchUpdate(
            name='# of living patients',
            initial_size=initial_pop_size,
            times_of_changes=self.survivalTimes,
            increments=[-1]*len(self.survivalTimes)
        )

