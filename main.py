from betting.betting_type import *
from betting.plot import plot_graph


if __name__ == '__main__':
    initial_wager = 100
    sample_size = 1000
    number_bets = 1000
    initial_funds = 10000
    multiple = 3

    single_bettor(initial_wager, sample_size, number_bets, initial_funds, 'k')
    # double_bettor(initial_wager, sample_size, number_bets, initial_funds, 'c')
    # multiple_bettor(initial_wager, sample_size, number_bets, initial_funds, multiple, 'r')
    # dAlembert(initial_wager, sample_size, number_bets, initial_funds, 'k')
    plot_graph('Account Value', 'Wager Count', initial_funds)
