import Problem5Inputs as Data
import SimPy.Plots.Histogram as Hist
import SimPy.Plots.SamplePaths as Path
from Simulate5 import Cohort

# create a cohort
myCohort = Cohort(id=1,
                  pop_size=Data.POP_SIZE,
                  transition_prob_matrix=Data.get_trans_prob_matrix(Data.TRANS_MATRIX))

# simulate the cohort over the specified time steps
myCohort.simulate(n_time_steps=Data.SIM_TIME_STEPS)

# plot the sample path (survival curve)
Path.plot_sample_path(
    sample_path=myCohort.cohortOutcomes.nLivingPatients,
    title='Survival Curve',
    x_label='Time-Step (Year)',
    y_label='Number Survived')

# plot the histogram of survival times
Hist.plot_histogram(
    data=myCohort.cohortOutcomes.survivalTimes,
    title='Histogram of Patient Survival Time',
    x_label='Survival Time (Year)',
    y_label='Count',
    bin_width=1)

# plot the histogram of the total number of strokes
Hist.plot_histogram(
    data=myCohort.cohortOutcomes.totalNumberOfStrokes,
    title='Histogram of Number of Strokes',
    x_label='Number of Strokes',
    y_label='Count',
    bin_width=1)


# print the patient survival time
print('Mean survival time (years):',
      myCohort.cohortOutcomes.meanSurvivalTime)
# print mean time to AIDS
print('Mean time until Post Stroke (years)',
      myCohort.cohortOutcomes.meanTimeToPostStroke)
# print the number of strokes
print('Number of strokes:',
      myCohort.cohortOutcomes.totalStrokes)