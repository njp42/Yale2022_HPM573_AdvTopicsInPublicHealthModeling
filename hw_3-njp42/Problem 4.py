from InstructorsComments import MultipleGames

EVENTS = 20
PROB = 0.5
GAMES = 1000

mygame = MultipleGames(id=0, num_games=GAMES, prob=PROB)
mygame.simulate(events=EVENTS)

print("The probability of loss is: " + str(mygame.calc_prob_loss()))
