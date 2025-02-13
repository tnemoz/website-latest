---
title: "Coding the AlphaZero search algorithm from scratch - Part 4: AlphaZero's improvements upon MCTS"
categories:
- Personal projects
tags:
- Machine Learning
series: AlphaZero
short_title: Implementing the MCTS algorithm
index_in_series: 4
---

### The Value Network and the Policy network
- The **Value Network**  gives a value representing how favorable is this game state for the current player. For instance, if the current player has a guaranteed win against their adversary, the value network would return 1. Conversely, if the network thinks they will lose 80% of the time in this position, then it may return -0.6. It doesn't matter if the number doesn't have a clear interpretation as "this is the probability of the current player winning the game". The only thing that matters is that if a situation A is more favorable for the current player than another situation B, then the value returned by the Value Network in situation A must be larger than that in situation B.
- The **Policy Network** assigns probabilities to all the possible actions our AI can take. Basically, we want this network to assign large probabilities to actions that lead to favorable outcomes for the current player.

Using these two networks, our goal is to determine the best action to take in this situation. You may wonder:
> "Wait, but isn't that the point of the Policy Network? Why do we even need a Value Network then?"

The key insight is to understand that the Policy Network only gives you an initial guess about where you should look at in the tree. The algorithm will follow this initial guess, and then use the Value Network to improve on this guess. Basically, it will tell the algorithm whether the position was actually good or not.

Now, the other question is: how do we even train these neural networks? What the AlphaGo team did was to download high-level games of Go and train both networks to mimic the players' behavior on these games. Then, once the AI reached a certain level, it was further trained by reinforcement learning by playing against itself. For AlphaZero however, the training of its neural networks (there's actually a single network with two heads, but I'll keep speaking in plural for simplicity) has been done solely using reinforcement learning.
