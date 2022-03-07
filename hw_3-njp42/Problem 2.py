from InstructorsComments import MultipleGames

EVENTS = 20
PROB = 0.6  #given prob defines tails probability, 1-prob(h) = prob(t)
GAMES = 1000

mygame = MultipleGames(id=0, num_games=GAMES, prob=PROB)

print("The expected value of the unfair coin is: " + str(mygame.simulate(events=EVENTS)))