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
The very first thing I've started working on upon starting my PhD is Pseudorandom Quantum States, or PRS for short. In particular, I realized that [in the proof of Brakerski and Shmueli](https://arxiv.org/abs/1906.10611), one inequality was unnecessarily large, meaning that we could improve the bound on the trace distance. It was *definitely* not worth writing anything about it, and so I forgot about it. Some time later, [Ananth, Gulati, Qian and Yuen provided a simpler proof of Brakerski and Shmueli's result](https://arxiv.org/abs/2211.01444), but it ended up beating the better bound that I found back then.

Even later (yeah I know, my narrative skills are exceptional), I realized that it was in fact possible to exactly compute not only the trace distance exactly, but also to compute the exact decomposition of the associated density matrix! What's more, the proof is arguably even simpler than Ananth *et. al*'s! The problem is that though I find this cool, it's definitely *not* something important enough to deserve a publication, so my advisors advised me (it's in the name) to simply write a blog post about it. So, here I am! First of all, let us start by defining the objects we'll be dealing with.

### Notations
In all this post, $d\geqslant2$, $t\geqslant1$ and $P\geqslant1$ will be three natural numbers. We denote $\omega_P$ the $P$-th root of unity, that is $\omega_P=\mathrm{e}^{\frac{2\mathrm{i}\pi}{P}}$. For a function $f:[d]\to[P]$, we define $\ket{\psi_f}$ to be

$$\begin{equation}\ket{\psi_f}\overset{\text{def}}{=}\frac{1}{\sqrt{d}}\sum_x\omega_P^{f(x)}\,\ket{x}\,.\end{equation}$$

We then define $\rho_{d, t, P}$ to be the average state $\ket{\psi_f}^{\otimes t}$ over all possible functions from $[d]$ to $[P]$. That is, we have

$$\begin{equation}
\newcommand\selfinner[1]{\left|#1\middle\rangle\!\middle\langle#1\right|}
\rho_{d, t, P}=\frac{1}{P^{d}}\sum_f\left(\selfinner{\psi_f}\right)^{\otimes t}\,.
\end{equation}$$ 

Finally, we will denote $\Pi_{d, t}$ the density matrix of $t$-copies of a Haar random state. That is, we have

$$\begin{equation}\Pi_{d, t}\overset{\text{def}}{=}\int_{U}\left(U\selfinner{0}U^\dagger\right)^{\otimes t}\,\mathrm{d}\mu(U)\end{equation}$$

with $\mu$ being the Haar measure on set of $d\times d$ unitary matrices. Our ultimate goal is to compute the trace distance between $\rho_{d, t, P}$ and $\Pi_{d, t}$. If these two are close even for a large number of copies like $\Omega\\!\left(\sqrt{d}\right)$, it would mean that the set of phase states is an Asymptotically Random State, as defined [here, in Definition 8](https://arxiv.org/abs/1906.10611). This in turn means that we could simply replace the random functions by a quantum-secure pseudorandom one, and voilà! You've got a PRS, [using which you can do cryptography](https://arxiv.org/abs/2112.10020).

We are now ready to give a bit more info on the introduction, and to talk about the bounds that were previously derived for the $P=2$ case, that is, the binary phases one.

## The binary phases state

### Known bounds
#### Brakerski and Shmueli
In order to talk about the first bound that was derived by Brakerski and Shmueli, we first have to talk about the bound that was derived by [Ji, Liu and Song in the original PRS article](https://eprint.iacr.org/2018/544). They showed that if $n$ was large enough, then

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2^n}-\Pi_{2^n,t}\right\|_1=\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{(N+1)(N+2)\cdots(N+t-1)}\end{equation}$$

where we've denoted $N=2^n$. Note that we have

$$\begin{equation}(N-1)(N-2)\cdots(N-t+1)=N^{t-1}-\frac{t(t-1)}{2}N^{t-2}+\Theta\!\left(t^4N^{t-3}\right)\end{equation}$$

and

$$\begin{equation}(N+1)(N+2)\cdots(N+t-1)=N^{t-1}+\frac{t(t-1)}{2}N^{t-2}+\Theta\!\left(t^4N^{t-3}\right)\,.\end{equation}$$

Using these two relations, a quick calculation gives

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2^n}-\Pi_{d, t}\right\|_1=\frac{t(t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

Now, what Brakerski and Shmueli did, instead of computing the trace distance between $\rho_{2^n, t, 2}$ and $\Pi_{d, t}$, is that they instead bound the trace distance between $\rho_{2^n,t, 2}$ and $\rho_{2^n,t, 2^n}$, and then used triangle inequality with the previous result to get back to $\Pi_{d, t}$. They managed to show the following bound:

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{(N+1)(N+2)\cdots(N+t-1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}\,.\end{equation}$$

They then simplified this bound to $\frac{4t^2}{2^n}$. However, using the previous relations, we can refine this bound to $\frac{t(t-1)}{2^n}+\Theta\\!\left(\frac{t^4}{2^{2n}}\right)$, which by triangle inequality finally gives us

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\Pi_{d, t}\right\|_1\leqslant\frac{3t(t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

#### Ananth, Gulati, Qian and Yuen
Ananth, Gulati, Qian and Yuen also make use of the triangle inequality, though not using the same density matrix as Brakerski and Shmueli. The bound they get by doing so is

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{(N+1)(N+2)\cdots(N+t-1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}+\frac{t^2}{N}\end{equation}$$

which reduces to

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{t(3t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

In particular, this bound is slightly better than Brakerski and Shmueli's. However, one of the trace distance in their computations may have a slightly better bound, and the use of triangle inequality prevents us from getting an exact result like in the case of $\rho_{2^n,t,2^n}$. The question now becomes: can we get an exact result?

### Computing the spectral decomposition of $\rho_{d, t, 2}$
#### Computing the density matrix
The very first thing one could do is to compute the coefficients of $\rho_{d, t, 2}$. We have

$$\newcommand\ketbra[2]{\left|#1\middle\rangle\!\middle\langle#2\right|}\begin{align}
    \rho_{d, t, 2} &= \frac{1}{d^t2^{d}}\sum_f\sum_{\substack{x_1,\cdots,x_t\\y_1,\cdots,y_t}}(-1)^{\bigoplus\limits_{i=1}^t\left[f\left(x_i\right)\oplus f\left(y_i\right)\right]}\,\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}\\
    &= \frac{1}{d^t2^{d}}\sum_{\substack{x_1,\cdots,x_t\\y_1,\cdots,y_t}}\left[\sum_f(-1)^{\bigoplus\limits_{i=1}^t\left[f\left(x_i\right)\oplus f\left(y_i\right)\right]}\right]\,\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}\\
\end{align}$$

Now, suppose there is some number $z$ that appears an odd number of times in $x\parallel y$, the concatenation of $x$ and $y$. You can convince yourself that the middle sum is going to be nil: for each function such that $f(z)=0$, we will also sum the exact same function $f'$ except at input $z$ where $f'(z)=1$, which would cancel out the first one. On the other hand, if no element appears an odd number of times, then the exponent of $-1$ is always going to be $0$, meaning that we will sum $1$ over all possible binary functions. All in all, we have

$$\begin{equation}
\rho_{d,t,2} = \frac{1}{d^t}\sum_{\substack{x_1,\cdots,x_t\\y_1,\cdots,y_t\\x\sim y}}\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}
\end{equation}$$

where $\sim$ is an equivalence relation on $[d]^t$, where $x\sim y$ if and only if no element $z$ of $[d]$ appears an odd number of times in $x\parallel y$. For conciseness' sake we will write

$$\begin{equation}
\rho_{d,t,2} = \frac{1}{d^t}\sum_{x\sim y}\ketbra{x}{y}
\end{equation}$$

where $x$ and $y$ are to be seen as elements of $[d]^t$. Let us now make a small detour that will be useful for both the binary phases state and the ones defined with other unit roots.

#### Spectral decomposition of matrices defined via an equivalence relation
Let $\sim$ be an equivalence relation on $[d]^t$. For an element $x$ of $[d]^t$, we denote $\mathcal{C}(x)$ its equivalence class with respect to $\sim$. We also define for such an element

$$\begin{equation}\ket{\mathcal{C}(x)}\overset{\text{def}}{=}\sum_{y\sim x}\ket{y}\,.\end{equation}$$

Let $\sigma$ be a density matrix that can be written as

$$\begin{equation}\sigma=\sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x}}\ketbra{x}{y}\end{equation}$$

with $\left\\{\alpha\_{\mathcal{C}(x)}\right\\}\_{x\in[d]^t}$ being arbitrary positive numbers that are constant across equivalence classes. Let us check what happens when we apply $\ket{\mathcal{C}(z)}$ to $\sigma$. We have

$$\begin{align}
    \sigma\ket{\mathcal{C}(z)} &= \sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x}}\ketbra{x}{y}\sum_{w\sim z}\ket{w}\\
    &= \sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x\\y\sim z}}\ket{x}\\
    &= \sum_{\substack{x\in[d]^t\\x\sim z}}\alpha_{\mathcal{C}(x)}\ket{x}\sum_{\substack{y\in[d]^t\\y\sim x}}1\\
    &= \sum_{\substack{x\in[d]^t\\x\sim z}}\alpha_{\mathcal{C}(x)}|\mathcal{C}(x)|\,\ket{x}\\
    &= \alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\sum_{\substack{x\in[d]^t\\x\sim z}}\ket{x}\\
    &= \alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\,\ket{\mathcal{C}(z)}\,.
\end{align}$$

Thus, for any $z\in[d]^t$, $\ket{\mathcal{C}(z)}$ is an eigenvector of $\sigma$ associated to the eigenvalue $\alpha_{\mathcal{C}(z)}\|\mathcal{C}(z)\|$. In order to consider a single element of each equivalence class, we can quotient $[d]^t$ by $\sim$. Note that there is no other eigenvectors associated to a non-zero eigenvalue since we have

$$\begin{equation}\mathrm{tr}[\sigma]=\sum_{z\in[d]^t}\alpha_{\mathcal{C}(z)}=\sum_{z\in[d]^t_{/\sim}}\alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\,.\end{equation}$$

Thus, we have found all the non-zero eigenvalues of $\sigma$. All in all, we can write $\sigma$ as

$$\begin{equation}\sigma = \sum_{z\in[d^t]_{/\sim}}\alpha_{\mathcal{C}(z)}|\mathcal{C}(z)|\,\selfinner{\mathcal{C}(z)}\,.\end{equation}$$

Let us now apply this to $\rho_{d, t, 2}$!

#### Computing the eigenvalues and their multiplicities
TODO

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
