---
layout: post
title: Finding all the eigenvalues of an observable using VQE and VQD
categories:
- Tutorials
tags:
- Quantum Computing
math: true
media_subpath: /assets/img/posts/VQE-VQD/
---
Upon working on a Pull Request for the `qiskit-algorithms` package, I stumbled upon its `VQD` class, which I'd never heard of, but was used to find all the eigenvalues of some observable, when VQE could only find the lowest one. So, I've read [the original paper](https://quantum-journal.org/papers/q-2019-07-01-156/) and thought that explaining it was also a good opportunity to explain VQE, since VQD can be seen as a generalization of it.

# VQE
## Problem statement
So first, let us explain what VQE is. The [Variational Quantum Eigensolver](https://www.nature.com/articles/ncomms5213) (VQE) is an algorithm used to find the lowest eigenvalue of an observable having a sparse Pauli decomposition. Let's stop here and explain all the terms first.

### Required math

An observable is an Hermitian matrix $O$, that is a matrix which is equal to its own conjugate transpose: $O=O^\dagger$. As per the spectral theorem, it can be diagonalized, and all its eigenvalues are real. That is, we can write

$$\newcommand\ket[1]{\left|#1\right\rangle}\newcommand\proj[1]{\left|#1\middle\rangle\!\middle\langle#1\right|}O=\sum_i\lambda_i\,\proj{\lambda_i}$$

with $\left\\{\lambda_i\right\\}_i$ being $O$'s eigenvalues and $\left\\{\ket{\lambda_i}\right\\}_i$ being the associated normalized eigenvectors.


# VQD
