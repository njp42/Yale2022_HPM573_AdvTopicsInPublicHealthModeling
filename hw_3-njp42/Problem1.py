from InstructorsComments import MultipleGames

EVENTS = 20
PROB = 0.5
GAMES = 1000

mygame = MultipleGames(id=0, num_games=GAMES, prob=PROB)

print("The expected value of the game is: " + str(mygame.simulate(events=EVENTS)))









