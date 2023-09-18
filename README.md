# Blackjack Game

This is a simple text-based implementation of the classic casino game, Blackjack. Play against an AI dealer and see if you can beat the odds!

## Table of Contents
- Features
- How to Play
- Installation
- Usage
- Future Improvements

## Features

- Minimalist text-based UI.
- Uses a standard deck of cards.
- Simple AI logic for the dealer.

## How to Play

- Players start with two cards and the goal is to have the sum of card values as close to 21 as possible, without exceeding it.
- Numbered cards (2-10) are worth their face value.
- Face cards (K, Q, J) are worth 10 points.
- Aces can be either 1 or 11 points, depending on what's beneficial for the player.
- After the initial deal, the player can choose to "Hit" (receive another card) or "Stay" (keep their current total).
- The dealer reveals one card to the player initially and decides to hit or stay based on its total (hits until 17 or higher).
- The player busts (loses instantly) if their total goes over 21. Similarly, if the dealer's total goes over 21, they bust and the player wins.
- If neither busts, then the one with the total closest to 21 at the end of the round wins.

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

This game requires Python to be installed on your system.


Clone the repository:
```sh
git clone https://github.com/xaniz/BlackJack
```

Navigate to the directory:


```sh
cd <directory-name>
```
