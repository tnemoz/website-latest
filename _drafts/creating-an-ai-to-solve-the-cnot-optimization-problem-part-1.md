---
title: Creating an AI to solve the CNOT optimization problem - Part 1
categories: [Research]
tags: [Machine Learning, Quantum Computing]
math: true
---

During a summer School in 2023, I had the occasion to listen to Simon Martiel presenting his work [Shallower CNOT circuits on realistic quantum hardware](https://arxiv.org/abs/2303.07302). In order to understand what the problem they tackle in this paper is, let us consider a small quantum circuit made of three CNOT gates:

{% dark_light_image image="generated-3-CNOT-circuit.svg";alt="A circuit with 3 qubits and 3 CNOT gates. The first one links 0 to 2, the second one 1 to 0 and the third one 1 to 2.";subtitle="A small example of a CNOT circuit that can be optimized" %}

Reasoning on the basis states, we see that this circuit sends $$ \ket{abc} $$ to $$\ket{a\oplus b, b, a\oplus b\oplus c} $$. Thus, it would also be possible to implement this circuit using only two CNOT gates like so:

{% dark_light_image image="generated-2-CNOT-circuit.svg";alt="A circuit with 3 qubits and 2 CNOT gates. The first one links 1 to 0 and the second one 0 to 2.";subtitle="An optimized version of the previous circuit" %}

Clearly, this implementation is preferable, since it uses less CNOT gates. Though reducing CNOT circuits like this is interesting *per se*, we also want our circuits to be executable on actual quantum computers. But on these computers, we may not be able to perform any CNOT gate we'd like. For instance, let us consider the following layout:

{% dark_light_image image="generated-3-qubits-line-layout.svg";alt="A representation of three qubits aligned, with the middle one connecting the other twos.";subtitle="3 qubits disposed as a line" %}

This layout is the worst-case scenario: the qubits are laid out as a straight line, which means that it is not possible to directly apply a CNOT between the qubits 0 and 2: we must connect them through qubit 1. For instance, we're not able to implement the optimized circuit above: it's impossible for us to perform a CNOT gate between qubits 0 and 2.

A simple way to deal with this problem is simply to apply SWAP gates like so:

$$
\langle\psi|\varphi\rangle
$$

Et là aussi

{% tabs test%}

{% tab test Python%}
```python
import numpy as np
for i in range(10):
    print(i)
# Un commentaire
```
{% endtab %}

{% tab test Rust %}
```rust
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World!");
}
```
{% endtab %}

{% endtabs %}

Puis voilà quoi!
{% tabs test%}

{% tab test Python%}
```python
import numpy as np
for i in range(10):
    print(i * 2000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
```
{: file='main.py'}
{% endtab %}

{% tab test Rust %}
```rust
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World aussi!");
}
```
{: file='main.rs'}
{% endtab %}

{% endtabs %}
