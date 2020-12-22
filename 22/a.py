DEBUG = False
class Deck(object):
    def __init__(self, id, cards=[]):
        # Index 0 is top of deck
        self.id = id
        self.cards = list(cards)

    def draw_from_top(self):
        return self.cards.pop(0)

    def add_to_top(self, new_cards):
        if type(new_cards) == int:
            self.cards.insert(0, new_cards)
        else:
            self.cards = new_cards + self.cards

    def add_to_bottom(self, new_cards):
        if type(new_cards) == int:
            self.cards.append(new_cards)
        else:
            self.cards = self.cards + new_cards

    def print(self):
        if not DEBUG: return
        print(self.id, ': ', sep='', end='')
        print(*self.cards, sep=' ')

    def score(self):
        return sum([(i+1)*c for i,c in enumerate(reversed(self.cards))])

    def deck_size(self):
        return len(self.cards)

class Game(object):
    def __init__(self, p1_cards, p2_cards):
        self.p1 = Deck('Player 1', p1_cards)
        self.p2 = Deck('Player 2', p2_cards)

    def simulate(self):

        players = {1:self.p1, 2:self.p2}

        while self.p1.deck_size() > 0 and self.p2.deck_size() > 0:

            c1, c2 = self.p1.draw_from_top(), self.p2.draw_from_top()
            if DEBUG: print("Cards drawn:", c1, c2)

            winner = 1 if c1 > c2 else 2
            cards = [c1,c2] if winner == 1 else [c2,c1]

            players[winner].add_to_bottom(cards)

            self.p1.print()
            self.p2.print()

            if DEBUG: print('Player {} wins the round!'.format(winner))

        score = players[winner].score()

        return winner, score

p1, p2 = Deck('Player 1'), Deck('Player 2')
players, cur = {1:p1, 2:p2}, 1

with open('input.txt') as f:
    for line in f.readlines():
        if line.strip().startswith('Player'):
            if line[7] == '2':
                cur = 2
            continue

        if line.strip().isnumeric():
            players[cur].add_to_bottom(int(line))

game = Game(p1.cards, p2.cards)
winner, score = game.simulate()

print('Player {} wins with score {}'.format(winner, score))