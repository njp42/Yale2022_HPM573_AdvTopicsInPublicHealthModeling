from InstructorsComments import MultipleGames
import SimPy.Plots.Histogram as Hist

EVENTS = 20
PROB = 0.5
GAMES = 1000

mygame = MultipleGames(id=0, num_games=GAMES, prob=PROB)

mygame.simulate(events=EVENTS)

# plot the histogram
Hist.plot_histogram(
    data=mygame.totalReward,
    title='Histogram of Patient Survival Time',
    x_label='Survival Time (Year)',
    y_label='Count')

print("The minimum is: " + str(min(mygame.totalReward)))
print("The maximum is: " + str(max(mygame.totalReward)))