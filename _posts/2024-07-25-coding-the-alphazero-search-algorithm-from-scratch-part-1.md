---
title: 'Coding the AlphaZero search algorithm from scratch - Part 1: Presentation
  of the MCTS algorithm'
categories:
- Personal projects
tags:
- Machine Learning
math: true
series: AlphaZero
media_subpath: /assets/img/posts/AlphaZero1/
short_title: Presentation of the MCTS algorithm
index_in_series: 1
date: 2024-07-25 20:24 +0200
---
One algorithm I've always been fascinated with is AlphaZero. I've wondered for quite some time how good it would be if I made it play other games. So, in order to figure it out, and to deepen my understanding of it, I decided to code it myself.

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

## Statement of the problem
Let us consider a turn-based game with a known list of actions the player is allowed to do. What we want to do is to choose the action that benefits the player the most in the long term. There is a very simple algorithm for that: we simply have to simulate all possibilities and choose the best one. In our situation, this would correspond to building a tree, where each node corresponds to a game state, and each branch corresponds to an action, transforming a game state into another.

The obvious downside to this is that we don't have the computational power to do this for most (interesting) games. For instance in the game of Go for which AlphaGo was developed in the first place, there are more than $2^{565}$ legal positions. Using an analogy [previously used in cryptography](https://www.schneier.com/blog/archives/2009/09/the_doghouse_cr.html), simply counting up to that number would require far, far more energy than what's contained in all the stars of all known galaxies. So, going through all the positions is out of the picture. What do we do then?

## The Monte-Carlo Tree Search algorithm
AlphaZero can be viewed as a modified version of the well-known Monte-Carlo Tree Search (or MCTS for short) algorithm. Thus, in order to understand it, we first have to describe this algorithm to then see how AlphaZero improves upon it.

In order to get a grasp on what the MCTS algorithm is about, let us consider the well-known game of Tic-Tac-Toe, and suppose you have to play the following position:

{% dark_light_image image="generated-tictactoe-first-position.svg";alt="A Tic-Tac-Toe grid with the first play being in the middle of the grid, and the second one being at the top middle.";subtitle="The starting position" %}

The idea of the MCTS algorithm is to perform a trade-off between exploring new potential solutions, and exploiting those that seem valuable. Just like the previous naive algorithm, we're going to build a tree of game states. But this time, we won't explore the whole tree. Instead, we'll try to detect the most interesting moves to play.

Each node in our tree will be given a value $v$. The higher this value, the most promising this node. However, even though we may want to explore further in the tree starting from this node, to check whether it really is interesting, we can't afford to spend all of our computational resources on it. So, we add a penalty: the more we visit a node, the less likely it is to be picked. A typical formula that we could use for this purpose is:

$$\text{Node score}=v+C\times\sqrt{\frac{\ln(N)}{n}}$$

with:
 - $v$ being the value of the node. For instance, this could be an estimated probability of winning the game if this node is selected, or a value ranging from $-1$ to $1$, with $-1$ indicating a strong chance of winning for the adversary and $1$ a strong chance of winning for us;
 - $C$ is a constant that allows us to foster either exploitation (for $C$ being low) or exploration (for $C$ being large). In the following examples, we will take $C=\sqrt{2}$;
 - $N$ is the total number of times the parent of the node has been visited;
 - $n$ is the number of times the node has been visited.

You can see that the higher the value $v$, the higher the node score. But on the other hand, the more this node is visited relatively to its siblings, the lowest its score. It thus act as a trade-off between exploration and exploitation. What we'll do is thus picking the node with the highest score. In case of a tie, we could select at random, or pick the first one, it doesn't really matter, since we would visit the other ones at some point too.


 1. *Selection.* Start from the root, which is the game state we're currently in. Select children according to the exploration/exploitation trade-off formula until a leaf is reached.

For now, in our example, our tree is only made of the root, so we directly reach a leaf. Let us continue the algorithm.

{:start="2"}
 2. *Expansion.* If the leaf isn't a terminal state, then create the possible children and choose one according to the trade-off formula.

Though in our case there are technically seven possible plays, we can use the fact that the position we're in is symmetric, so that we really only have to explore four of them:

{% dark_light_image image="generated-tictactoe-initial-tree.svg";alt="A tree with Tic-Tac-Toe grids, with the root representing the previous initial position. It has four children, placing a cross on the north-west, west, south-west and south case respectively. Each branch is associated with the score of infinity and each grid has their statistics shown near them, allowing to compute their score.";subtitle="Tree of possible plays from the root";width="100000" %}

The branches here contain the node score. Since the nodes have never been visited, it results in a division by 0. Setting their score to $+\infty$ ensures that we will visit each of them at least once. For the example's sake, let us say that we've randomly selected the second child.

{:start="3"}
 3. *Rollout.* Starting from the child we selected, we now simulate a game by playing random moves until a terminal state is reached.

In our case, let us assume that we won this simulation. We are now ready for the last step of the algorithm.

{:start="4"}
 4. *Backpropagation.* Update the information in the tree according to the result of the rollout.

So, in our case, this will mean that for all the nodes we've visited during this iteration, we will change their value so that it represents an estimation of the probability of winning starting from this state. That is, the value for a node will be equal to $v=\frac{w-d}{n}$, with $w$ being the number of victories in a rollout containing this state, and $d$ being the number of defeats. In our case, this would lead to the following tree:

{% dark_light_image image="generated-tictactoe-second-tree.svg";alt="A tree with Tic-Tac-Toe grids, with the root representing the previous initial position. It has four children, placing a cross on the north-west, west, south-west and south case respectively. Each branch is associated with the score of infinity except the second one which is associated with the score of 0.";subtitle="Updated tree of possible plays after a single iteration";width="100000" %}

You may have noticed something strange: the value $v$ of the root got updated to $-1$ instead of $1$. That's not a mistake on my part! The thing to remember here is that each level of the tree represents the game state for a given player. But if the player playing with the crosses wins, it means that the other one lost! A potentially counterintuitive fact is that the value of a node must be high if the player playing this position has a good chance to *lose* the game.

This point is not trivial at all, be sure to understand it before going on. One way to think about it is the following: when a node looks at its children, it wants to select the one leading to the best estimated probability of success for the player whose turn it is. So it means that the value that a node holds doesn't represent the probability of winning for the player who is to play, but for its adversary!

For instance, in our case, since it is our turn to play and the state we're in is represented by the root, it means that the lower the value of the root, the more comfortable we are, since this value is associated with our adversary's probability of success.

Now that we've covered this, we finally repeat this process a large number of times to get a good estimate of the probabilities of winning for each node. Just to be sure, let's do a few more iterations by hand. Clearly, the next iterations are going to select the children with an infinite score. Let us say for instance that the rollout for the first child resulted in a draw, and that the ones for the last two children resulted in a loss. The tree will then look like this:

{% dark_light_image image="generated-tictactoe-third-tree.svg";alt="The same tree as previously, with the statistics having been updated, and the scores being respectively a half + 2 times the square root of the logarithm of 2 for the first two branch, 1 + 2 times the square root of the logarithm of 2 for the second one and 2 times the square root of the logarithm of 2 for the last two ones.";subtitle="Updated tree of possible plays after four iterations";width="100000" %}

We now see that the algorithm will favor the second child. We will thus create its children like so:

{% dark_light_image image="generated-tictactoe-fourth-tree.svg";alt="The same tree as previously, with the statistics being shown for the root and the selected child. The scores of the children on the second level are all infinite.";subtitle="Updated tree of possible plays during the fifth iteration";width="100000" %}

Note that for clarity's sake, I've removed the statistics of the irrelevant nodes from the picture, but they of course conserve their statistics throughout the algorithm. For this last step, let us assume that the first child has been randomly selected and that his rollout ended up in a win for the player playing crosses. Since this player is also the one playing this position, this represents a defeat for this node. Similarly, it will be counted as a win for the node on the first level, and as a defeat for the root, so that the tree at the end of the fifth iteration looks like this:

{% dark_light_image image="generated-tictactoe-fifth-tree.svg";alt="The same tree as previously, with the statistics being shown for the root and the selected child. The scores of the children on the second level are all infinite except for the first one which is 1 + square root of 2 times the logarithm of 2.";subtitle="Updated tree of possible plays after the fifth iteration";width="100000" %}

As a sanity check, we observe that by simulating a win for the player playing crosses, it increased the value of the node at the first level of the tree. Thus, this node is more likely to be explored and selected at the end, since it seems to be more likely to lead to victory.

Once a large number of iterations has been performed, we select the node with the highest visit counts as our play. You may wonder why don't we simply select the node with the highest value instead: you definitely can. The two strategies generally lead to the same results except in very special cases, where the strategy using the visit counts performs slightly better.

## Discussion

Before moving on to the implementation, I'd like to answer some legitimate concerns concerning this algorithm:
> How do we choose the value of $C$?

$C$ is what is generally called in machine learning an *hyperparameter*. That's a fancy term to say: make a guess and hope for the best. Now, there *are* methods that allows to tune hyperparameters, but for conciseness' sake I won't talk about them here.
> Why should this algorithm work in a real-world scenario, where the adversary doesn't play at random?

Intuitively, this algorithm will guide you to sections of the search space where most of the situations are favorable to you. Plus, the closer you are to the end of the game, the less space there is for variance: if a not-too-far guaranteed win is feasible, it should be found if the number of simulations isn't too low.

But this logic only gets you so far. The deeper you are in the game, the more performant MCTS is. This means that for a game like chess with a huge branching factor, the first moves chosen by the MCTS algorithm won't be really that interesting: the search space is just too large for the value to have a low variance. Basically, for a huge branching factor, the MCTS algorithm will play random moves during the first iterations, until the point where its estimates become reasonably trustworthy.
> How to deal with random events?

It depends on how frequently these events happen. A possibility that we'll use in the implementation is to compute the game states on-the-fly rather than storing them. That is, what you're really interested about isn't the game state, but the actions that led to this game state. By doing so, when computing the game state, you can include these random events, the nodes would still store the average probability of winning.

However, if these random events are frequent, then the number of simulations that you perform may not be sufficiently large to accurately represent the average value of a node. Putting it differently, the variance you'll have in this estimation will be too high to be useful in practice.

Now that that's said, let's move on to implementing this algorithm for a well-known game: chess!
