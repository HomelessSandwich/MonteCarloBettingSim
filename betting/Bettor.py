from random import randint


class Bettor:

    def __init__(self, initial_funds, colour):
        self.initial_funds = initial_funds
        self.funds = initial_funds
        self.colour = colour
        self.win_previous = True
        self.funds_history = []

    @staticmethod
    def bet_outcome():
        roll = randint(1, 100)
        if roll <= 50:
            return False
        else:
            return True

    @property
    def broke(self):
        if self.funds == 0:
            return True
        else:
            return False

    @property
    def profit(self):
        return self.funds - self.initial_funds

    def bet(self, wager):
        if self.funds < wager:
                wager = self.funds
        if self.bet_outcome():
            self.win_previous = True
            self.funds += wager
        else:
            self.win_previous = False
            self.funds -= wager
        self.plot_point()

    def plot_point(self):
        self.funds_history.append(self.funds)
