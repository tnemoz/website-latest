---
title: 'Coding the AlphaZero search algorithm from scratch - Part 2: Implementing
  the MCTS algorithm'
categories:
- Personal projects
tags:
- Machine Learning
series: AlphaZero
short_title: Implementing the MCTS algorithm
index_in_series: 2
date: 2024-08-15 15:50 +0200
---
Now that we've seen in the previous article how the MCTS algorithms works, let us implement it on a simple game: Tic-Tac-Toe!

> This post is part of a series about AlphaZero. You can find the other posts here.{% assign series_post = site.posts | where: "series", page.series | sort: "index_in_series" %}{% for post in series_post %}
> - {% if post.title == page.title %}Part {{ page.index_in_series }}: {{ page.short_title }}{% else %}[Part {{ post.index_in_series }}: {{ post.short_title }}]({{ site.baseurl }}{{ post.url }}){% endif %}{% endfor %}
{: .prompt-tip }
Now that we have seen how the algorithm works, let us implement it!

#### Implementing a generic MCTS algorithm
First of all, we have to represent what a game state is, and what we should be able to do with it. This includes:
 - Determining whether a game state is terminal, and returning the winner if it is;
 - Get the list of all possible actions from this game state;
 - Computing the game state resulting from the application of an action on the current game state.

Right away, we see that we'll also need to represent what an action is. Since we want to be as generic as possible, we *almost* don't require anything from an action. We will only require that it implements the `__eq__` and `__hash__` dunder methods, so that one can search an `Action` in a list:
```python
from abc import ABC, abstractmethod
from typing import Self


class Action(ABC):
    """Represent a generic possible action a player can do in a game."""

    @abstractmethod
    def __eq__(self: Self, other: Self) -> bool:
        """Test equality between two Actions."""
        pass

    @abstractmethod
    def __hash__(self: Self) -> int:
        """Return a unique hash value for this Action."""
        pass

```
{: file='action.py' }
Now that we have our `Action` defined, let us move to the game state. This essentially boils down to listing everything our game state is supposed to be able to do.

A small remark here: we'll assume that it's possible to know which player is to play the position using internal data. For instance, if you were to represent a chess game, you could put positive numbers to represent the pieces the current player owns, negative ones for that of the other player, and then multiply the while board by -1 when you transition from one game state to another (along with potentially flipping it upside-down).

```python
from abc import ABC, abstractmethod
from typing import Optional, Self

from action import Action


class GameState(ABC):
    """Abstract class to represent a game state.

    It is assumed that the player playing the position can be identified using some internal data.
    For instance, the player whose turn it is could have their pieces represented by positive
    numbers, while the other one would have their pieces represented by negative numbers.
    """

    @abstractmethod
    def get_winner(self: Self) -> Optional[int]:
        """Return the winner of the game, if it exists.

        If the current game state isn't terminal, then None is returned. Otherwise, it returns:
        - 1 if player playing this position won.;
        - -1 if the other player won;
        - 0 in case of a draw.
        """
        pass

    @abstractmethod
    def get_possible_actions(self: Self) -> list[Action]:
        """Return the list of possible actions when playing this game state."""
        pass

    @abstractmethod
    def transition(self: Self, action: Action) -> Self:
        """Return the new game state resulting from a given action applied on the current state."""
        pass

```
{: file='game_state.py' }

Though they don't seem to be useful, these two files will allow a user to simply define the inner workings of the game they're interested in without worrying about the MCTS implementation. Speaking of which, let us start to code it! The very first thing we want to do here is to represent a node in our tree. Using this node, we want to be able to:
 - Access and update the node's statistics, namely its number of visits, wins and loss;
 - Access its parent, in order to get its visit count;
 - Compute its value and UCB score;
 - Determining whether this node is a leaf;
 - Perform the four steps of the MCTS algorithm.

First of all, let's initialize it:
```python
from math import sqrt
from typing import Self, Optional

from action import Action


class _Node:
    """Represent a node in the MCTS tree."""

    # Constant that represents the exploration/exploitation trade-off
    C: float = sqrt(2)

    @classmethod
    def set_trade_off_constant(cls: type(Self), value: float) -> None:
        """Update the value of the exploration/exploitation trade-off constant."""
        cls.C = value

    def __init__(self: Self, parent: Optional[Self]) -> None:
        """Initialize the node.

        :param parent: Parent node in the MCTS tree.
        """
        self.parent: Optional[Self] = parent

        self.children: list[_Node] = []
        self.actions: list[Action] = []
        self.visits: int = 0
        self.n_wins: int = 0
        self.n_defeats: int = 0
```
{: file='mcts.py' .nolineno }

You may have noted that the nodes don't know which player they are associated with. Indeed, storing this value for each node would be quite wasteful in space. The trick here is that we assumed that we can retrieve the player that is to play the position from the game state. Stating it differently, a game state always represent the position as seen by the player whose turn it is.

Similarly, the nodes themselves are oblivious to the state they represent: the state is instead computed on-the-fly each time. There are two reasons for that:
 - it allows to not store the game states, which can get pretty memory-heavy;
 - it allows to include random events, as mentioned in the first part of this series.

Of course, this comes at a computational cost, and if for a given application the game states can be efficiently stored, then it might be worth a shot to try to store them directly in the nodes.

First of all, let us start with the computation of a `Node`'s value. This is a simple one: we simply have to apply the formula that was mentioned earlier. We just have to take care to check whether this node has ever been visited to avoid a division by 0.

```python
    @property
    def value(self: Self) -> float:
        """Return the value of the node."""
        if self.visits == 0:
            return 0

        return return (self.n_wins - self.n_defeats) / self.visits
```
{: file='mcts.py' .nolineno }

Similarly, we can implement the `ucb` property. Since we'll use a logarithm, we first import it from the `math` module:
```python
from math import sqrt, log
```
{: file='mcts.py' .nolineno }
We can now implement the `ucb` property:
```python
    @property
    def ucb(self: Self) -> float:
        """Return the USB score of this Node."""
        if self.visits == 0:
            return float("inf")

        # No need to check for the parent's visit count to be positive, since it is necessarily
        # larger than that of its child
        return self.value + self.C * sqrt(log(self.parent.visits) / self.visits)
```
{: file='mcts.py' .nolineno }
The `is_leaf` property also doesn't offer much difficulty: a node is a leaf if it hasn't any child by definition.
```python
    @property
    def is_leaf(self: Self) -> bool:
        """Return True if this Node is a leaf node."""
        return len(self.children) == 0
```
{: file='mcts.py' .nolineno }
We now move to the `select_child` method. It seems natural to code this function in a recursive way, because trees generally work naturally well with it. The first thing we have to do is import the `GameState` we've previously created for typing purposes:
```python
from game_state import GameState
```
{: file='mcts.py' .nolineno }
Now, for the recursion, the base case is simple: we stop as soon as we hit a leaf:
```python
    def select_child(self: Self, state: GameState) -> tuple[Self, GameState]:
        """Recursively select a leaf using the exploration/exploitation trade-off formula."""
        if self.is_leaf:
            return self, state
```
{: file='mcts.py' .nolineno }
If we're not at a leaf, we want to find all the children with the maximal score along with the corresponding action. This can be simply done using the `key` argument of the built-in `max` function:
```python
        best_child, best_action = max(
            zip(self.children, self.actions),
            key=lambda child_action: child_action[0].ucb,
        )
```
{: file='mcts.py' .nolineno }
Now that we have our best child, we just have to recursively call its own `select_child` method to go one step further. Of course, we mustn't forget to compute the next state. Putting everything together, we arrive at the following function:
```python
    def select_child(self: Self, state: GameState) -> tuple[Self, GameState]:
        """Recursively select a leaf using the exploration/exploitation trade-off formula."""
        if self.is_leaf:
            return self, state

        best_child, best_action = max(
            zip(self.children, self.actions),
            key=lambda child_action: child_action[0].ucb,
        )

        return best_child.select_child(state.transition(best_action))
```
{: file='mcts.py' .nolineno }
Let us move on to the `expand` function. We know that this function is only called on leaves, and its goal is to create its children. However, we must first ensure that that node we're at isn't terminal, in which case we want it to stay a leaf.

In order to create its children, we simply have to list all the possible actions from this game state and create the associated nodes.

The only thing we need to take care about is the fact that if the node is terminal, then `state` doesn't change, while if we create a child and select it, it does. Since we're going to select the new child at random, we'll need the `choice` function from the `random` module:
```python
from random import choice
```
{: file='mcts.py' .nolineno }

All in all, this leads to the following function:
```python
    def expand(self: Self, state: GameState) -> tuple[Self, GameState]:
        """Expand this Node by listing all the possible actions and randomly choose a child."""
        # If the state is terminal, we don't expand the associated node
        if state.get_winner() is not None:
            return self, state

        self.actions = state.get_possible_actions()
        self.children = [_Node(self) for _ in self.actions]
        chosen_child, chosen_action = choice(list(zip(self.children, self.actions)))

        return chosen_child, state.transition(chosen_action)
```
{: file='mcts.py' .nolineno }
We now have to implement the `rollout` method. There's not really any catch in this one: we simply play random moves until a winner (or a draw) is found.
The implementation is then straightforward:
```python
    @staticmethod
    def rollout(state: GameState) -> int:
        """Perform the rollout phase of the MCTS.

        This function randomly selects moves until a terminal game state is reached from this state.
        Once such a state has been reached, this function will return:
        - 1 if it resulted in a win for the player playing this position;
        - -1 if it resulted in a loss for the player playing this position;
        - 0 if it resulted in a draw.
        """
        new_state = state
        player = 1

        while (winner := new_state.get_winner()) is None:
            random_action = choice(new_state.get_possible_actions())
            new_state = new_state.transition(random_action)
            player *= -1

        return winner * player
```
{: file='mcts.py' .nolineno }
Finally, we only have to implement the backpropagation to finish our implementation of a node. There are three things to do on a node:
 - Increment its visit count;
 - Increase its number of draws if the rollout result is a draw, or its number of wins if the rollout value *doesn't* match the player to play in this position;
 - Recursively backpropagate if we're not at the root.

All in all, this leads to the following implementation:
```python
    def backpropagate(self: Self, rollout_value: int) -> None:
        """Backpropagate the rollout result through the tree.

        This function performs the backpropagation phase of the MCTS algorithm. It updates the value
        of the nodes according to the player playing in their position and the rollout result.

        :param rollout_value: The value of the rollout result. It is equal to 0 if the current 
          player won, 1 if the other player won, and 0.5 in case of a draw.
        """
        self.visits += 1

        # If the current player wins the rollout, then this node's value must decrease
        # This is because intuitively, the current player is the adversary of the player that will
        #   look at this node
        if rollout_value == -1:
            self.n_wins += 1
        elif rollout_value:
            self.n_defeats += 1

        # Unless we're at the root of the tree
        if self.parent is not None:
            self.parent.backpropagate(-rollout_value)
```
{: file='mcts.py' .nolineno }
We'll also add a `__repr__` dunder method for good measure, so that debugging is a little bit easier:
```python
    def __repr__(self: Self) -> str:
        value = self.value
        visits = self.visits

        return f"_Node({value=}, {visits=})"
```
{: file='mcts.py' .nolineno }
Let us now move to the `MCTS` class. During its initilization, we need to:
 - Set the trade-off constant to a given value;
 - Initialize the root;
 - Set the number of iterations per play.

All in all, this leads to the following implementation:
```python
class MCTS:
    """A class used to perform an MCTS algorithm."""
    def __init__(
        self: Self,
        state: GameState,
        trade_off_constant: float,
        n_simulations: int,
    ) -> None:
        """Initialize the MCTS algorithm.

        This function sets the global parameters used by the MCTS algorithm and initialize it.

        :param state: The state the game starts in.
        :param trade_off_constant: The trade-off constant as used in the UCB formula.
        :param n_simulations: The number of simulations that are performed from the root.
        """
        _Node.set_trade_off_constant(trade_off_constant)
        self.root = _Node(None)
        self.root_state = state
        self.n_simulations = n_simulations
```
{: file='mcts.py' .nolineno }

We then went to add a `transition` function that will take an `Action` as argument and progress in the tree accordingly to this `Action`. This is also straightforward: we simply have to fetch the child corresponding to this action and change both the `root` and the `root_state:
```python
    def transition(self: Self, action: Action) -> None:
        """Advance the game with a given action.

        This function allows to progress in the game tree without any computation. This may for
        example prove useful if the adversary is exterior to this class.
        """
        index = self.root.actions.index(action)

        self.root = self.root.children[index]
        self.root_state = self.root_state.transition(action)
```
{: file='mcts.py' .nolineno }
Note that this is where we need to have `__eq__` and/or `__hash__` defined for an `Action`: so that the `index` method can look for a given `Action`.

Last but not least, the `decide` method will glue together everything we've done up to now to actually make a decision. First of all, we want to perform our simulations:
```python
        node = self.root

        for _ in trange(self.n_simulations):
            node, state = node.select_child(self.root_state)
            node, state = node.expand(state)
            rollout_value = node.rollout(state)
            node.backpropagate(rollout_value)
            node = self.root
```
{: file='mcts.py' .nolineno }
We now want to fetch the index of the child having the largest visit counts. Once again, it's possible to use the built-in `max` function along with the `enumerate` generator for that:
```python
        chosen_action = self.root.actions[
            max(enumerate(self.root.children), key=lambda x: x[1].visits)[0]
        ]
```
{: file='mcts.py' .nolineno }
Finally, if `advance` is set to `True`, we want to change the `root` along with the player associated to it. In all cases, we return the action to take. All i all, this is the final implementation of the `decide` method:
```python
    def decide(self: Self, advance: bool = True) -> Optional[Action]:
        """Decide the next move to be played.

        This function performs a number of simulation as specified in the algorithm initialization,
        updating the nodes' scores along the way. Once these simulations have been performed, it
        selects the best child to go with according to its visit counts.

        :param advance: If set to True, in addition to returning the best action, the root will be
          set to the child corresponding to this action.
        """
        node = self.root

        for _ in trange(self.n_simulations):
            node, state = node.select_child(self.root_state)
            node, state = node.expand(state)
            rollout_value = node.rollout(state)
            node.backpropagate(rollout_value)
            node = self.root

        chosen_action = self.root.actions[
            max(enumerate(self.root.children), key=lambda x: x[1].visits)[0]
        ]

        if advance:
            self.transition(chosen_action)

        return chosen_action
```
{: file='mcts.py' .nolineno }

Let us now give a quick example on how to use this code to create an AI for Tic-Tac-Toe. First, we have to represent what an action and a game state are in this case. The former is quickly done, it only needs to hold the `x` and `y` coordinates of the play.

```python
class TicTacToeAction(Action):
    """A Tic-Tac-Toe action."""

    def __init__(self: Self, x: int, y: int) -> None:
        """Initialize the action."""
        self.x = x
        self.y = y

    def __eq__(self: Self, other: Self):
        return self.x == other.x and self.y == other.y

    def __hash__(self: Self):
        return 3 * self.x + self.y

    def __repr__(self: Self) -> str:
        """Return a string representation of the action."""
        return f"Action({self.x}, {self.y})"
```
{: file='tictactoe.py' .nolineno }
Note that here, creating a hash function is simple enough, since it's easy to assign a unique value to a pair of numbers that are upper-bounded. In the general case, Python's built-in `hash` function would do the job if the `Action` is more complicated.

Concerning the game state in itself, we'll simply represent it with a `numpy` array, with each coefficient of the matrix being `1` if the current player played at this position, `-1` if the adversary of the current player played in this position, and `0` otherwise. This representation allows us to easily flip the perspective of the board from one player to another, and will also allow us to have efficient checks to determine whether a player won.

By doing so, there's not much difficulty in implementing the required methods: one simply has to
 - take care of every possible case in the `get_winner` method;
 - list all the empty squares for the `get_possible_actions` method;
 - set a matrix element for the `transition` method.

All in all, this leads to the following implementation:
```python
class TicTacToeGameState(GameState):
    """A Tic-Tac-Toe game state."""

    def __init__(
        self: Self, initial_state: Optional[npt.NDArray[np.int8]] = None
    ) -> None:
        """Initialize the game state."""
        if initial_state is None:
            self.board: npt.NDArray[np.int8] = np.zeros((3, 3), dtype=np.int8)
        else:
            if initial_state.shape != (3, 3):
                raise ValueError(
                    "Wrong shape provided for initial state. "
                    f"Expected (3,3) and got {initial_state.shape}"
                )

            self.board = initial_state

    def get_winner(self: Self) -> Optional[int]:
        check_col = self.board.sum(axis=0)
        check_row = self.board.sum(axis=1)
        check_diag = np.trace(self.board)
        check_anti_diag = np.trace(np.fliplr(self.board))

        if -3 in check_col or -3 in check_row or check_diag == -3 or check_anti_diag == -3:
            return -1

        if 0 not in self.board:
            return 0

    def get_possible_actions(self: Self) -> list[Action]:
        return [
            TicTacToeAction(int(y), int(x)) for x, y in np.argwhere(self.board == 0)
        ]

    def transition(self: Self, action: TicTacToeAction) -> Self:
        new_state = TicTacToeGameState(self.board.copy())
        new_state.board[action.y, action.x] = 1
        new_state.board *= -1

        return new_state

    def __repr__(self: Self) -> str:
        """Return a string representation of the game state."""
        res = ""
        for row in self.board:
            res += "|".join(("X" if x == 1 else "O") if x else " " for x in row) + "\n"

        # Remove last \n
        return res[:-1]
```
{: file='tictactoe.py' .nolineno }
I've also added a `__repr__` method to better visualize the state computed by the algorithm.

A small remark on the `get_winner` function: you may wonder why we don't check for a win for the current player. The reason for that is that Tic-Tac-Toe, along with many board games, has this nice property that it isn't possible for a player to win by a move of its adversary. Thus, since a game state always represents the position as seen by the player who is to play it, it isn't possible to start in a position where the last move made us won! This is clearly a negligible optimization, but on more complex games with this property, this could prove useful.

And we're done! For instance, in order to determine which move to play in the first position given as an example in the previous article, one would do it like so:
```python
import numpy as np

from mcts import MCTS
from tictactoe import TicTacToeGameState

initial_state = np.array(
    [
        [0, -1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
)

mcts_player = MCTS(TicTacToeGameState(initial_state), np.sqrt(2), 800)
action = mcts_player.decide(advance=False)

print(mcts_player.root_state.transition(action))

```
{: file='main.py' }
Now that we have seen the MCTS algorithm, we'll see in the next article how AlphaZero improves upon it.

