---
layout: post
title: Exactly computing the trace distance between phase states and Haar random ones
categories:
- Research
tags:
- Quantum Information
- Pseudorandom Quantum States
math: true
media_subpath: /assets/img/posts/Trace-Distance-Phase-States
---
## Introduction
### Prologue
The very first thing I've started working on upon starting my PhD is Pseudorandom Quantum States, or PRS for short. In particular, I realized that [in the proof of Brakerski and Shmueli](https://arxiv.org/abs/1906.10611), one inequality was unnecessarily large, meaning that we could improve the bound on the trace distance. It was *definitely* not worth writing anything about it, and so I forgot about it. Some time later, [Ananth, Gulati, Qian and Yuen provided a simpler proof of Brakerski and Shmueli's result](https://arxiv.org/abs/2211.01444), though their bound was slightly worse than the one I found back then.

Even later (yeah I know, my narrative skills are exceptional), I realized that it was in fact possible to exactly compute not only the trace distance exactly, but also to compute the exact decomposition of the associated density matrix! What's more, the proof is arguably even simpler than Ananth *et. al*'s! The problem is that though I find this cool, it's definitely *not* something important enough to deserve a publication, so my advisors advised me (it's in the name) to simply write a blog post about it. So, here I am! First of all, let us start by defining the objects we'll be dealing with.

### Notations
In all this post, $d\geqslant2$, $t\geqslant1$ and $P\geqslant1$ will be three natural numbers. We denote $\omega_P$ the $P$-th root of unity, that is $\omega_P=\mathrm{e}^{\frac{2\mathrm{i}\pi}{P}}$. For a function $f:[d]\to[P]$, we define $\ket{\psi_f}$ to be

$$\begin{equation}\ket{\psi_f}\overset{\text{def}}{=}\frac{1}{\sqrt{d}}\sum_{x=0}^{d-1}\omega_P^{f(x)}\,\ket{x}\,.\end{equation}$$

We then define $\rho_{d, t, P}$ to be the average state $\ket{\psi_f}^{\otimes t}$ over all possible functions from $[d]$ to $[P]$. That is, we have

$$\begin{equation}
\newcommand\selfinner[1]{\left|#1\middle\rangle\!\middle\langle#1\right|}
\rho_{d, t, P}=\frac{1}{P^{d}}\sum_{f\in[P]^{[d]}}\left(\selfinner{\psi_f}\right)^{\otimes t}\,.
\end{equation}$$ 

Finally, we will denote $\Pi_{d, t}$ the density matrix of $t$-copies of a Haar random state. That is, we have

$$\begin{equation}\Pi_{d, t}\overset{\text{def}}{=}\int_{U\in\mathcal{U}(d)}\left(U\selfinner{0}U^\dagger\right)^{\otimes t}\,\mathrm{d}\mu(U)\end{equation}$$

with $\mu$ being the Haar measure on $\mathcal{U}(d)$, the set of $d\times d$ unitary matrices. Our ultimate goal is to compute the trace distance between $\rho_{d, t, P}$ and $\Pi_{d, t}$. If these two are close even for a large number of copies like $\Omega\\!\left(\sqrt{d}\right)$, it would mean that the set of phase states is an Asymptotically Random State, as defined [here, in Definition 8](https://arxiv.org/abs/1906.10611). This in turn means that we could simply replace the random functions by a quantum-secure pseudorandom one, and voilà! We've got ourselves a PRS, [using which you can do cryptography](https://arxiv.org/abs/2112.10020).

We are now ready to give a bit more info on the introduction, and to talk about the bounds that were previously derived for the $P=2$ case, that is, the binary phases one.

## Known bounds for the binary phases states
### Brakerski and Shmueli
In order to talk about the first bound that was derived by Brakerski and Shmueli, we first have to talk about the bound that was derived by [Ji, Liu and Song in the original PRS article](https://eprint.iacr.org/2018/544) for the $P=2^n$ case. They showed that if $n$ was large enough, then

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2^n}-\Pi_{2^n,t}\right\|_1=\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{(N+1)(N+2)\cdots(N+t-1)}\end{equation}$$

where we've denoted $N=2^n$. Note that we have

$$\begin{equation}(N-1)(N-2)\cdots(N-t+1)=N^{t-1}-\frac{t(t-1)}{2}N^{t-2}+\Theta\!\left(t^4N^{t-3}\right)\end{equation}$$

and

$$\begin{equation}(N+1)(N+2)\cdots(N+t-1)=N^{t-1}+\frac{t(t-1)}{2}N^{t-2}+\Theta\!\left(t^4N^{t-3}\right)\,.\end{equation}$$

Using these two relations, a quick calculation gives

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2^n}-\Pi_{d, t}\right\|_1=\frac{t(t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

Now, what Brakerski and Shmueli did, instead of computing the trace distance between $\rho_{2^n, t, 2}$ and $\Pi_{d, t}$, is that they instead bounded the trace distance between $\rho_{2^n,t, 2}$ and $\rho_{2^n,t, 2^n}$, and then used triangle inequality with the previous result to get back to $\Pi_{d, t}$. They managed to show the following bound:

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{(N+1)(N+2)\cdots(N+t-1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}\,.\end{equation}$$

They then simplified this bound to $\frac{4t^2}{2^n}$. However, using the previous relations, we can refine this bound to $\frac{t(t-1)}{2^n}+\Theta\\!\left(\frac{t^4}{2^{2n}}\right)$, which by triangle inequality finally gives us

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\Pi_{d, t}\right\|_1\leqslant\frac{3t(t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

### Ananth, Gulati, Qian and Yuen
Ananth, Gulati, Qian and Yuen also make use of the triangle inequality, though not using the same density matrix as Brakerski and Shmueli. The bound they get by doing so is

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{(N+1)(N+2)\cdots(N+t-1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}+\frac{t^2}{N}\end{equation}$$

which reduces to

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{t(3t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

In particular, this bound is slightly worse than the improvement over Brakerski and Shmueli's. However, one of the trace distance in their computations may have a slightly better bound, and the use of triangle inequality prevents us from getting an exact result like in the case of $\rho_{2^n,t,2^n}$. The question now becomes: can we get an exact result?

## Spectral decomposition of matrices defined via an equivalence relation
Let us first make a small detour that will almost immediately gives us the result we want. Let $\sim$ be an equivalence relation on $[d]^t$. For an element $x$ of $[d]^t$, we denote $\mathcal{C}(x)$ its equivalence class with respect to $\sim$. We also define for such an element

$$\begin{equation}\ket{\mathcal{C}(x)}\overset{\text{def}}{=}\sum_{y\sim x}\ket{y}\,.\end{equation}$$

Let $\sigma$ be a density matrix that can be written as

$$\begin{equation}\label{eq:density-matrix-equivalence}\sigma=\sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x}}\ketbra{x}{y}\end{equation}$$

with $\left\\{\alpha\_{\mathcal{C}(x)}\right\\}\_{x\in[d]^t}$ being arbitrary positive numbers that are constant across equivalence classes. Let us check what happens when we apply $\ket{\mathcal{C}(z)}$ to $\sigma$. We have

$$\begin{align}
    \sigma\ket{\mathcal{C}(z)} &= \sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x}}\ketbra{x}{y}\sum_{w\sim z}\ket{w}\\
    &= \sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x\\y\sim z}}\ket{x}\\
    &= \sum_{\substack{x\in[d]^t\\x\sim z}}\alpha_{\mathcal{C}(x)}\ket{x}\sum_{\substack{y\in[d]^t\\y\sim x}}1\\
    &= \sum_{\substack{x\in[d]^t\\x\sim z}}\alpha_{\mathcal{C}(x)}|\mathcal{C}(x)|\,\ket{x}\\
    &= \alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\sum_{\substack{x\in[d]^t\\x\sim z}}\ket{x}\\
    &= \alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\,\ket{\mathcal{C}(z)}\,.
\end{align}$$

Thus, for any $z\in[d]^t$, $\ket{\mathcal{C}(z)}$ is an eigenvector of $\sigma$ associated to the eigenvalue $\alpha_{\mathcal{C}(z)}\|\mathcal{C}(z)\|$. In order to consider a single element of each equivalence class, we can quotient $[d]^t$ by $\sim$. Note that there are no other eigenvectors associated to a non-zero eigenvalue since we have

$$\begin{equation}\mathrm{tr}[\sigma]=\sum_{z\in[d]^t}\alpha_{\mathcal{C}(z)}=\sum_{z\in[d]^t_{/\sim}}\alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\end{equation}$$

and since we have $\langle\mathcal{C}(x)\|\mathcal{C}(y)\rangle\neq0\iff x\sim y$. Thus, we have found all the non-zero eigenvalues of $\sigma$. All in all, we can write $\sigma$ as

$$\begin{equation}\label{eq:spectral-decomposition-equivalence}\sigma = \sum_{z\in[d^t]_{/\sim}}\alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\,\selfinner{\mathcal{C}(z)}\,.\end{equation}$$

Let us now apply this to $\rho_{d, t, 2}$, and then to the other phase states!

## The binary phases state
### Computing the density matrix
The very first thing one could do is to compute the coefficients of $\rho_{d, t, 2}$. We have

$$\newcommand\ketbra[2]{\left|#1\middle\rangle\!\middle\langle#2\right|}\begin{align}
    \rho_{d, t, 2} &= \frac{1}{d^t2^{d}}\sum_{f\in[2]^[d]}\sum_{\substack{x_1,\cdots,x_t\in[d]\\y_1,\cdots,y_t\in[d]}}(-1)^{\bigoplus\limits_{i=1}^t\left[f\left(x_i\right)\oplus f\left(y_i\right)\right]}\,\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}\\
    &= \frac{1}{d^t2^{d}}\sum_{\substack{x_1,\cdots,x_t\in[d]\\y_1,\cdots,y_t\in[d]}}\left[\sum_f(-1)^{\bigoplus\limits_{i=1}^t\left[f\left(x_i\right)\oplus f\left(y_i\right)\right]}\right]\,\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}\\
\end{align}$$

Now, suppose there is some number $z$ that appears an odd number of times in $x\parallel y$, the concatenation of $x$ and $y$. You can convince yourself that the middle sum is going to be nil: for each function such that $f(z)=0$, we will also sum the exact same function $f'$ except at input $z$ where $f'(z)=1$, which would cancel out the first one. On the other hand, if no element appears an odd number of times, then the exponent of $-1$ is always going to be $0$, meaning that we will sum $1$ over all possible binary functions. All in all, we have

$$\begin{equation}
\rho_{d,t,2} = \frac{1}{d^t}\sum_{\substack{x_1,\cdots,x_t\in[d]\\y_1,\cdots,y_t\in[d]\\x\sim y}}\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}
\end{equation}$$

where $\sim$ is an equivalence relation on $[d]^t$, where $x\sim y$ if and only if no element $z$ of $[d]$ appears an odd number of times in $x\parallel y$. For conciseness' sake we will write

$$\begin{equation}
\rho_{d,t,2} = \frac{1}{d^t}\sum_{x\sim y}\ketbra{x}{y}
\end{equation}$$

where $x$ and $y$ are to be seen as elements of $[d]^t$. Thus, since we know that a density matrix that can be written according to Equation \eqref{eq:density-matrix-equivalence} can be diagonalized according to Equation \eqref{eq:spectral-decomposition-equivalence}, we only have to study the aforementioned equivalence relation to find the eigenvalues of $\rho_{d, t, 2}$ and their associated multiplicities!

### Computing the eigenvalues and their multiplicities
So, what are the equivalence classes of the aforementioned equivalence relation? Let us fix an element $i\in[d]$. If $x\in[d]^t$ contains an odd number of $i$, then $y\in[d]^t$ also has to contain an odd number of $i$, so that the total number of $i$ in their concatenation is even. Similarly, if $x$ contained an even number of $i$, then so does $y$ if $x\sim y$.

Let us define $n_i(x, y)$ to count the number of $i\in[d]$ in the concatenation of $x$ and $y$. The equivalence relation $\sim$ is defined via

$$\begin{equation}x\sim y\iff n_i(x, y)=0\pmod2\,.\end{equation}$$

For instance, let us consider $d=4$ and $t=6$, and let us consider the element $x=(0, 3, 1, 3, 2, 1)$. We observe that $0$ and $2$ appear an odd number of times, meaning that if an element $y$ is in relation with $x$, it must also have an odd number of $0$ and $2$. So for instance, the following elements belong in $\mathcal{C}(x)$:
 - $(0, 2, 0, 0, 2, 2)$;
 - $(1, 0, 1, 2, 1, 1)$;
 - $(0, 3, 1, 3, 1, 2)$.

So, we can see that what we really care about to count the number of tuples that are in relation to another is the number of elements in this tuple that appear an odd number of times. One way to see this is that in order to generate all the tuples that are in relation with $x$, we can first place $0$ and $2$ once, resulting in $(0, 2, \cdot, \cdot, \cdot)$. We can then pick an element from $[4]$, including $0$ and $2$, and we fill the next two places of the tuple with this element. For instance, let's say that we picked $1$, resulting in $(0, 2, 1, 1, \cdot, \cdot)$. We then reiterate this last step until the tuple is filled, resulting in for instance $(0, 2, 1, 1, 0, 0)$. Finally, we can consider all unique permutations of this tuple.

This process can generate, for a given $x\in[d]^t$, all the elements $y$ that are in relation with $x$. In particular, it allows us to count $\|\mathcal{C}(x)\|$! It also allows us to uniquely identify an equivalence class: an equivalence class is uniquely identified by the elements that appear an odd number of times in any of its tuple. For instance, taking back $x=(0, 3, 1, 3, 2, 1)$, $\mathcal{C}(x)$ is uniquely identified by $\\{0, 2\\}$.

Another thing we can notice is that $\|\mathcal{C}(x)\|$ will only depend on the **length** of its identifier. This can be seen by the fact that the elements in $[d]$ can play symmetric roles: for instance, for any tuple in $\mathcal{C}(x)$, we can generate exactly one tuple belonging in the equivalence class identified by $\\{0, 1\\}$ be replacing $2$ by $1$ and vice-versa. In particular, there's a bijection between these two finite sets, meaning that they have the same size.

So, let us start by fixing some natural number $k\leqslant t$, and let us count the number of elements in an equivalence class uniquely identified by $k$ elements. Note that $k$ necessarily has the same parity as $t$. Indeed, suppose that $k$ is odd for instance. Since it counts the number of unique elements that appear an odd number of times, it necessarily means that the number of these elements is odd in any tuple. But now, all the other elements must appear an even number of times, which necessarily means that $t$ must be odd. Similarly, if $k$ is even, then so must be $t$.

Without loss of generality, let us assume that the elements from $[k]$ appear an odd number of times, while the others appear an even number of times.

## The other phase states
TODO

## Cite this blog post
```bibtex
@online{NemozBlogPost|{{ page.name | truncate: 15, "" }},
  author={Tristan Nemoz},
  title={% raw %}{{% endraw %}{{ page.title }}{% raw %}}{% endraw %},
  date={% raw %}{{% endraw %}{{ page.date | date: '%Y-%m-%d' }}{% raw %}}{% endraw %},
  url={% raw %}{{% endraw %}{{ page.url | absolute_url }}{% raw %}}{% endraw %},
  urldate={% raw %}{{% endraw %}{{ 'now' | date: '%Y-%m-%d' }}{% raw %}}{% endraw %}
}
```
