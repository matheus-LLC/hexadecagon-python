"""
Interesting idea here:
The question is, should you take a bet on a fair coin when heads gives you $130
while tails makes you lose $100?

If the answer is yes, this program should give some insight on how long one should play.
"""

import random


def wallet_after_gamble(wallet_value, number_of_plays, win_price, lose_price):
    for i in range(number_of_plays):
        if random.randint(0, 1):
            wallet_value += win_price
        else:
            wallet_value -= lose_price
    return wallet_value


def main():
    outcomes_list = []
    win_price = 130
    lose_price = 100
    for j in range(0, 100):
        outcomes_list.append(wallet_after_gamble(0, j, win_price, lose_price))
    print(outcomes_list)


if __name__ == '__main__':
    main()
