from .Bettor import Bettor
from .ui import *
import matplotlib.pyplot as plt


def single_bettor(wager, sample_size, number_bets, initial_funds, colour):
    num_broke = 0
    num_profitors = 0
    profits = []
    loses = []

    for i in range(sample_size):
        bettor = Bettor(initial_funds, colour)
        bettor.plot_point()
        for i in range(number_bets):
            if not bettor.broke:
                bettor.bet(wager)
            else:
                num_broke += 1
                break
        if bettor.profit > 0:
            num_profitors += 1
            profits.append(bettor.profit)
        else:
            loses.append(bettor.profit)
        plt.plot(range(len(bettor.funds_history)), bettor.funds_history, colour)
    print_stats(num_broke, num_profitors, sample_size, profits, loses, 'Single Bettor')


def double_bettor(wager, sample_size, number_bets, initial_funds, colour):
    num_broke = 0
    num_profitors = 0
    profits = []
    loses = []


    for i in range(sample_size):
        bettor = Bettor(initial_funds, colour)
        bettor.plot_point()
        for i in range(number_bets):
            if not bettor.broke:
                if bettor.win_previous:
                    bettor.bet(wager)
                else:
                    bettor.bet(2 * wager)
            else:
                num_broke += 1
                break
        if bettor.profit > 0:
            num_profitors += 1
            profits.append(bettor.profit)
        else:
            loses.append(bettor.profit)
        plt.plot(range(len(bettor.funds_history)), bettor.funds_history, bettor.colour)

    print_stats(num_broke, num_profitors, sample_size, profits, loses, 'Double Bettor')


def multiple_bettor(wager, sample_size, number_bets, initial_funds, multiple, colour):
    num_broke = 0
    num_profitors = 0
    profits = []
    loses = []

    for i in range(sample_size):
        bettor = Bettor(initial_funds, colour)
        bettor.plot_point()
        for i in range(number_bets):
            if not bettor.broke:
                if bettor.win_previous:
                    bettor.bet(wager)
                else:
                    bettor.bet(wager * multiple)
            else:
                num_broke += 1
                break
        if bettor.profit > 0:
            num_profitors += 1
            profits.append(bettor.profit)
        else:
            loses.append(bettor.profit)
        plt.plot(range(len(bettor.funds_history)), bettor.funds_history, bettor.colour)
    print_stats(num_broke, num_profitors, sample_size, profits, loses, 'Rand Multiple Bettor')


def dAlembert(wager, sample_size, number_bets, initial_funds, colour):
    num_broke = 0
    num_profitors = 0
    initial_wager = wager
    prev_wager = wager
    profits = []
    loses = []

    for i in range(sample_size):
        bettor = Bettor(initial_funds, colour)
        bettor.plot_point()

        for i in range(number_bets):
            wager = initial_wager
            if not bettor.broke:
                if bettor.win_previous:
                    if wager != initial_wager:
                        wager -= prev_wager
                    bettor.bet(wager)
                else:
                    wager = prev_wager + initial_wager
                    bettor.bet(wager)
                    if not bettor.win_previous:
                        prev_wager = wager
            else:
                num_broke += 1
                break
        if bettor.profit > 0:
            num_profitors += 1
            profits.append(bettor.profit)
        else:
            loses.append(bettor.profit)
        plt.plot(range(len(bettor.funds_history)), bettor.funds_history, colour)
    print_stats(num_broke, num_profitors, sample_size, profits, loses, "D'Alembert Bettor")
