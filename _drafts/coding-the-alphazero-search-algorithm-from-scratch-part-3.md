---
title: 'Coding the AlphaZero search algorithm from scratch - Part 3: Improving the MCTS algorithm'
categories:
- Personal projects
tags:
- Machine Learning
math: false
series: AlphaZero
media_subpath: /assets/img/posts/AlphaZero3/
short_title: Improving the MCTS algorithm
index_in_series: 3
---
In this article, we'll see how to improve our previous implementation of the MCTS algorithm to strengthen our AI agent. Ideally, we would like it to beat weak chess adversaries, which it clearly isn't capable of at the moment.

> This post is part of a series about AlphaZero. You can find the other posts here.{% assign series_post = site.posts | where: "series", page.series | sort: "index_in_series" %}{% for post in series_post %}
> - {% if post.title == page.title %}Part {{ page.index_in_series }}: {{ page.short_title }}{% else %}[Part {{ post.index_in_series }}: {{ post.short_title }}]({{site.baseurl }}{{ post.url }}){% endif %}{% endfor %}
{: .prompt-tip }

> Parts of this series, be they on historical points or on code, have been inspired by several tutorials that you can find here:
> - [A step-by-step look at Alpha Zero and Monte Carlo Tree Search](https://joshvarty.github.io/AlphaZero/) by Josh Varty.
> - [A Simple Alpha(Go) Zero Tutorial](https://suragnair.github.io/posts/alphazero.html) by Surag Nair.
> - [AlphaZero explained](https://nikcheerla.github.io/deeplearningschool/2018/01/01/AlphaZero-Explained/) by Nikhil Cheerla.
> - [AlphaGo Zero Explained in One Diagram](https://medium.com/applied-data-science/alphago-zero-explained-in-one-diagram-365f5abf67e0) by David Foster.
> - [Lessons From Implementing AlphaZero](https://medium.com/oracledevs/lessons-from-implementing-alphazero-7e36e9054191) by Aditya Prasad.
> - [Quite a lot of posts from the AI StackExchange](https://ai.stackexchange.com).
{: .prompt-info }

## Pruning the tree
The main problem of our algorithm for now is that its number of simulations doesn't allow it to look that deep in the tree. Let us take back the game position taken at the end of the previous article:
![Checkmate in 2 for white. FEN: r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0](matein2.svg){: width="100%" }
And let us rerun the code to try to solve it, while adding a seed for reproducibility:
``python
from math import sqrt
from random import seed

from chess import Board

from game_state_chess import GameStateChess
from mcts import MCTS

seed(42)

initial_board = Board(fen="r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0")
mcts_player = MCTS(GameStateChess(initial_board), sqrt(2), 800)
action = mcts_player.decide(advance=False)
print(action)

```
{: file='test_puzzle.py '}
Now that we've ran this code, we can inspect the state of the tree to see how the AI is thinking:
```python
```
