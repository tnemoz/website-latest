---
layout: post
title: Exactly computing the trace distance between binary phase states and Haar random
  ones
categories:
- Research
tags:
- Quantum Information
- Pseudorandom Quantum States
math: true
media_subpath: "/assets/img/posts/Trace-Distance-Phase-States"
date: 2025-03-09 16:40 +0100
---
## Introduction
### Prologue
The very first thing I've worked on upon starting my PhD is Pseudorandom Quantum States, or PRS for short. In particular, I realized that [in the proof of Brakerski and Shmueli](https://arxiv.org/abs/1906.10611), one inequality was unnecessarily loose, meaning that we could improve the bound on the trace distance. It was *definitely* not worth writing anything about it, and so I forgot about it. Some time later, [Ananth, Gulati, Qian and Yuen provided a simpler proof of Brakerski and Shmueli's result](https://arxiv.org/abs/2211.01444), though their bound was slightly worse than the one I found back then.

Even later (yeah I know, my narrative skills are exceptional), I realized that it was in fact possible to exactly compute not only the trace distance exactly, but also the exact decomposition of the associated density matrix! What's more, the proof is arguably even simpler than Ananth *et al.*'s! The problem is that though I find this cool, it's definitely *not* something important enough to deserve a publication, so my advisors advised me (it's in the name) to simply write a blog post about it. So, here I am! First of all, let us start by defining the objects we'll be dealing with.

### Notations
Throughout this post, $d\geqslant2$, $t\geqslant1$ and $P\geqslant1$ will be three natural numbers. We denote by $\omega_P$ the $P$-th root of unity, that is $\omega_P=\mathrm{e}^{\frac{2\mathrm{i}\pi}{P}}$. For a function $f:[d]\to[P]$, we define $\ket{\psi_f}$ to be

$$\begin{equation}\ket{\psi_f}\overset{\text{def}}{=}\frac{1}{\sqrt{d}}\sum_{x=0}^{d-1}\omega_P^{f(x)}\,\ket{x}\,.\end{equation}$$

We then define $\rho_{d, t, P}$ to be the average state $\ket{\psi_f}^{\otimes t}$ over all possible functions from $[d]$ to $[P]$. That is, we have

$$\begin{equation}
\newcommand\selfinner[1]{\left|#1\middle\rangle\!\middle\langle#1\right|}
\rho_{d, t, P}\overset{\text{def}}{=}\frac{1}{P^{d}}\sum_{f\in[P]^{[d]}}\left(\selfinner{\psi_f}\right)^{\otimes t}\,.
\end{equation}$$ 

Finally, we will denote $\Pi_{d, t}$ the density matrix of $t$-copies of a Haar random state. That is, we have

$$\begin{equation}\Pi_{d, t}\overset{\text{def}}{=}\int_{U\in\mathcal{U}(d)}\left(U\selfinner{0}U^\dagger\right)^{\otimes t}\,\mathrm{d}\mu(U)\end{equation}$$

with $\mu$ being the Haar measure on $\mathcal{U}(d)$, the set of $d\times d$ unitary matrices. Our ultimate goal is to compute the trace distance between $\rho_{d, t, P}$ and $\Pi_{d, t}$. If these two are close even for a large number of copies like $\Omega\\!\left(\sqrt{d}\right)$, it would mean that the set of phase states is an Asymptotically Random State, as defined [here, in Definition 8](https://arxiv.org/abs/1906.10611). This in turn means that we could simply replace the random functions by a quantum-secure pseudorandom one, and voilà! We've got ourselves a PRS, [using which one can do cryptography](https://arxiv.org/abs/2112.10020).

We are now ready to give a bit more info on the introduction, and to talk about the bounds that were previously derived for the $P=2$ case, that is, the binary phases one.

## Known bounds for the binary phases state
### Brakerski and Shmueli
In order to talk about the first bound that was derived by Brakerski and Shmueli, we first have to talk about the bound that was derived by [Ji, Liu and Song in the original PRS article](https://eprint.iacr.org/2018/544) for the $d=P=2^n$ case. They showed that if $n$ was large enough, then

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2^n}-\Pi_{2^n,t}\right\|_1=\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{(N+1)(N+2)\cdots(N+t-1)}\end{equation}$$

where we've denoted $N=2^n$. Note that we have

$$\begin{equation}\label{eq:asymptoticsproduct1}(N-1)(N-2)\cdots(N-t+1)=N^{t-1}-\frac{t(t-1)}{2}N^{t-2}+\Theta\!\left(t^4N^{t-3}\right)\end{equation}$$

and

$$\begin{equation}\label{eq:asymptoticsproduct2}(N+1)(N+2)\cdots(N+t-1)=N^{t-1}+\frac{t(t-1)}{2}N^{t-2}+\Theta\!\left(t^4N^{t-3}\right)\,.\end{equation}$$

Using these two relations, a quick calculation gives

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2^n}-\Pi_{d, t}\right\|_1=\frac{t(t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

Now, instead of computing the trace distance between $\rho_{2^n, t, 2}$ and $\Pi_{d, t}$, Brakerski and Shmueli bounded the trace distance between $\rho_{2^n,t, 2}$ and $\rho_{2^n,t, 2^n}$, and then used the triangle inequality with the previous result to get back to $\Pi_{d, t}$. They managed to show the following bound:

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{(N+1)(N+2)\cdots(N+t-1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}\,.\end{equation}$$

They then simplified this bound to $\frac{4t^2}{2^n}$. However, using the previous relations, we can refine this bound to $\frac{t(t-1)}{2^n}+\Theta\\!\left(\frac{t^4}{2^{2n}}\right)$, which by triangle inequality finally gives us

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\Pi_{d, t}\right\|_1\leqslant\frac{3t(t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

### Ananth, Gulati, Qian and Yuen
Ananth, Gulati, Qian and Yuen also make use of the triangle inequality, though not using the same density matrix as Brakerski and Shmueli. The bound they got by doing so is

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{(N+1)(N+2)\cdots(N+t-1)}{N^{t-1}}-\frac{(N-1)(N-2)\cdots(N-t+1)}{N^{t-1}}+\frac{t^2}{N}\end{equation}$$

which reduces to

$$\begin{equation}\frac12\left\|\rho_{2^n,t,2}-\rho_{2^n,t,2^n}\right\|_1\leqslant\frac{t(3t-1)}{2^{n+1}}+\Theta\!\left(\frac{t^4}{2^{2n}}\right)\,.\end{equation}$$

In particular, this bound is slightly worse than our improvement over Brakerski and Shmueli's. However, one of the trace distances in their computations may have a slightly better bound, and the use of triangle inequality prevents us from getting an exact result like in the case of $\rho_{2^n,t,2^n}$. The question now becomes: can we get an exact result?

## Spectral decomposition of matrices defined via an equivalence relation
Let us first make a small detour that will almost immediately give us the result we want. Let $\sim$ be an equivalence relation on $[d]^t$. For an element $x$ of $[d]^t$, we denote $\mathcal{C}(x)$ its equivalence class with respect to $\sim$. For such an element, we also define

$$\begin{equation}\ket{\mathcal{C}(x)}\overset{\text{def}}{=}\sum_{y\sim x}\ket{y}\,.\end{equation}$$

Let $\sigma$ be a density matrix that can be written as

$$\begin{equation}\label{eq:density-matrix-equivalence}\sigma=\sum_{x\in[d]^t}\alpha_{\mathcal{C}(x)}\sum_{\substack{y\in[d]^t\\y\sim x}}\ketbra{x}{y}\end{equation}$$

with $\left\\{\alpha\_{\mathcal{C}(x)}\right\\}\_{x\in[d]^t}$ being arbitrary positive numbers that are constant across equivalence classes. Let us detrmine what happens when we apply $\ket{\mathcal{C}(z)}$ to $\sigma$. We have

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

Let us now apply this to $\rho_{d, t, 2}$!

## The binary phases state
### Computing the density matrix
The very first thing one could do is to compute the coefficients of $\rho_{d, t, 2}$. We have

$$\newcommand\ketbra[2]{\left|#1\middle\rangle\!\middle\langle#2\right|}\begin{align}
    \rho_{d, t, 2} &= \frac{1}{d^t2^{d}}\sum_{f\in[2]^[d]}\sum_{\substack{x_1,\cdots,x_t\in[d]\\y_1,\cdots,y_t\in[d]}}(-1)^{\bigoplus\limits_{i=1}^t\left[f\left(x_i\right)\oplus f\left(y_i\right)\right]}\,\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}\\
    &= \frac{1}{d^t2^{d}}\sum_{\substack{x_1,\cdots,x_t\in[d]\\y_1,\cdots,y_t\in[d]}}\left[\sum_f(-1)^{\bigoplus\limits_{i=1}^t\left[f\left(x_i\right)\oplus f\left(y_i\right)\right]}\right]\,\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}\\
\end{align}$$

Now, suppose there is some number $z$ that appears an odd number of times in $x\parallel y$, the concatenation of $x$ and $y$. You can convince yourself that the middle sum is going to be nil: for each function such that $f(z)=0$, we will also sum the exact same function $f'$ except at input $z$ where $f'(z)=1$, which would cancel out the first one. On the other hand, if no element appears an odd number of times, then the exponent of $-1$ is always going to be $0$, meaning that the sum evaluates to the number of all possible binary functions. All in all, we have

$$\begin{equation}
\rho_{d,t,2} = \frac{1}{d^t}\sum_{\substack{x_1,\cdots,x_t\in[d]\\y_1,\cdots,y_t\in[d]\\x\sim y}}\ketbra{x_1,\cdots,x_t}{y_1,\cdots,y_t}
\end{equation}$$

where $\sim$ is an equivalence relation on $[d]^t$, where $x\sim y$ if and only if no element $z$ of $[d]$ appears an odd number of times in $x\parallel y$. For conciseness' sake we will write

$$\begin{equation}
\rho_{d,t,2} = \frac{1}{d^t}\sum_{x\sim y}\ketbra{x}{y}
\end{equation}$$

where $x$ and $y$ are to be seen as elements of $[d]^t$. Thus, since we know that a density matrix that can be written according to Equation \eqref{eq:density-matrix-equivalence} can be diagonalized according to Equation \eqref{eq:spectral-decomposition-equivalence}, we only have to study the aforementioned equivalence relation to find the eigenvalues of $\rho_{d, t, 2}$ and their associated multiplicities!

### Computing the eigenvalues and their multiplicities
So, what are the equivalence classes of the aforementioned equivalence relation? Let us fix an element $i\in[d]$. If $x\in[d]^t$ contains an odd number of $i$, then $y\in[d]^t$ also has to contain an odd number of $i$, so that the total number of $i$ in their concatenation is even. Similarly, if $x$ contains an even number of $i$, then so does $y$ if $x\sim y$.

Let us define $n_i(x, y)$ to count the number of $i\in[d]$ in the concatenation of $x$ and $y$. The equivalence relation $\sim$ is defined via

$$\begin{equation}x\sim y\iff n_i(x, y)=0\pmod2\,.\end{equation}$$

For instance, let us take $d=4$ and $t=6$, and let us consider the element $x=(0, 3, 1, 3, 2, 1)$. We observe that $0$ and $2$ appear an odd number of times, meaning that if an element $y$ is in relation with $x$, it must also have an odd number of $0$ and $2$. So for instance, the following elements belong in $\mathcal{C}(x)$:
 - $(0, 2, 0, 0, 2, 2)$;
 - $(1, 0, 1, 2, 1, 1)$;
 - $(0, 3, 1, 3, 1, 2)$.

So, we can see that what we really care about in order to count the number of tuples that are in relation to another is the number of elements in this tuple that appear an odd number of times. One way to see this is that in order to generate all the tuples that are in relation with $x$, we can first place $0$ and $2$ once, resulting in $(0, 2, \cdot, \cdot, \cdot)$. We can then pick an element from $[4]$, including $0$ and $2$, and we fill the next two places of the tuple with this element. For instance, let's say that we picked $1$, resulting in $(0, 2, 1, 1, \cdot, \cdot)$. We then reiterate this last step until the tuple is filled, resulting in for instance $(0, 2, 1, 1, 0, 0)$. Finally, we can consider all unique permutations of this tuple.

This process can generate, for a given $x\in[d]^t$, all the elements $y$ that are in relation with $x$. In particular, it allows us to count $\|\mathcal{C}(x)\|$! It also allows us to uniquely identify an equivalence class: an equivalence class is uniquely identified by the elements that appear an odd number of times in any of its tuple. For instance, taking back $x=(0, 3, 1, 3, 2, 1)$, $\mathcal{C}(x)$ is uniquely identified by $\\{0, 2\\}$.

Another thing we can notice is that $\|\mathcal{C}(x)\|$ will only depend on the **length** of its identifier. This can be seen by the fact that the elements in $[d]$ can play symmetric roles: for instance, for any tuple in $\mathcal{C}(x)$, we can generate exactly one tuple belonging to the equivalence class identified by $\\{0, 1\\}$ by replacing $2$ by $1$ and vice-versa. In particular, there's a bijection between these two finite sets, meaning that they have the same size.

So, let us start by fixing some natural number $k\leqslant t$, and let us count the number of tuples in an equivalence class uniquely identified by $k$ elements. Note that $k$ necessarily has the same parity as $t$. Indeed, suppose that $k$ is odd for instance. Since it counts the number of unique elements that appear an odd number of times, it necessarily means that the number of these elements is odd in any tuple. But now, all the other elements must appear an even number of times, which necessarily means that $t$ must be odd. Similarly, if $k$ is even, then so must be $t$. So, let us redefine $k$ such that $k\leqslant\left\lfloor\frac{t}{2}\right\rfloor$, and let us count the number of tuples in an equivalence class uniquely identified by $2k+b$ elements, with $b$ being the parity of $t$, meaning that $b=0$ if $t$ is even, and $b=1$ otherwise.

Without loss of generality, let us assume that the elements from $[2k+b]$ appear an odd number of times, while the others appear an even number of times. One way to count these tuples is the following: we first choose how many times does $0$ appear, how many times $1$ appear, etc... with the constraint that all elements from $0$ to $2k+b-1$ included must appear an odd number of times. Let us denote $y_{i+1}$ the number of times $i$ appears in the tuple. The sum over the $y_i$ must also equal $t$. And finally, we must count the number of unique permutations of this tuple, which is $\frac{t!}{\prod_iy_i!}$. All in all, the eigenvalue associated to this equivalence class is

$$\begin{equation}\lambda_{d, t, 2k+b}=\frac{1}{d^t}\sum_{\substack{y_1,\cdots,y_{d}\\y_{1},\cdots,y_{2k+b}\text{ odd}\\y_{2k+b+1},\cdots,y_d\text{ even}\\\sum\limits_iy_i=t}}\frac{t!}{\prod\limits_iy_i!}\,.\end{equation}$$

Of course, the question now becomes: can we simplify this monstrosity a bit? Well, it turns out we (more or less) can using Newtown's multinomial formula! The computations are a bit tedious, and we won't use this "simplified" expression to compute the trace distance, so feel free to directly go to the final expression in Equation \eqref{eq:eigvalbin}. Still, if you somehow need this expression and are looking for a proof, here you go.

Let us define $S_i$ and $T_i$ to be

$$\begin{align}
S_i\left(x_1,\cdots,x_d\right) &= \sum_{\substack{y_1,\cdots,y_{d}\\y_{d-i+1},\cdots,y_{d}\text{ even}\\\sum\limits_iy_i=t}}t!\prod_i\frac{x_i^{y_i}}{y_i!}\,,\\
T_i\left(x_1,\cdots,x_d\right) &= \sum_{\substack{y_1,\cdots,y_{d}\\y_{d-i+2},\cdots,y_{d}\text{ even}\\y_{d-i+1}\text{ odd}\\\sum\limits_iy_i=t}}t!\prod_i\frac{x_i^{y_i}}{y_i!}\,.\\
\end{align}$$

Note that we have

$$\begin{align}
S_i\left(x_1,\cdots,x_d\right)+T_i\left(x_1,\cdots,x_d\right) &= S_{i-1}\left(x_1,\cdots,x_d\right)\,,\\
S_i\left(x_1,\cdots,x_d\right)-T_i\left(x_1,\cdots,x_d\right) &= S_{i-1}\left(x_1,\cdots,-x_{d-i+1},\cdots,x_d\right)\,.
\end{align}$$

This gives us

$$\begin{equation}S_i\left(x_1,\cdots,x_d\right)=\frac{1}{2}S_{i-1}\left(x_1,\cdots,x_d\right)+\frac{1}{2}S_{i-1}\left(x_1,\cdots,-x_{d-i+1},\cdots,x_d\right)\end{equation}$$

and thus

$$\begin{equation}\label{eq:tprimei0}S_i\left(x_1,\cdots,x_d\right)=\frac{1}{2^i}\sum_{j\in\{0, 1\}^i}S_0\left(x_1,\cdots,x_{d-i},(-1)^{j_1}x_{d-i+1},\cdots,(-1)^{j_i}x_d\right)\end{equation}$$

with

$$\begin{equation}S_0\left(x_1,\cdots,x_d\right)=\left(\sum_ix_i\right)^t\end{equation}$$

by Newton's multinomial formula. Let us now define $S'\_{i,j}$ and $T'\_{i,j}$ to be

$$\begin{align}
S'_{i,j}\left(x_1,\cdots,x_d\right)&=\sum_{\substack{y_1,\cdots,y_d\\y_{d-i-j+1}\text{ even}\\y_{d-i-j+2},\cdots,y_{d-i}\text{ odd}\\y_{d-i+1},\cdots,y_d\text{ even}\\\sum\limits_iy_i=t}}t!\prod_i\frac{x_i^{y_i}}{y_i!}\\
T'_{i,j}\left(x_1,\cdots,x_d\right)&=\sum_{\substack{y_1,\cdots,y_d\\y_{d-i-j+1},\cdots,y_{d-i}\text{ odd}\\y_{d-i+1},\cdots,y_d\text{ even}\\\sum\limits_iy_i=t}}t!\prod_i\frac{x_i^{y_i}}{y_i!}
\end{align}$$

with $S'\_{i, 0}=T'\_{i,0}=S_i$. We then have

$$\begin{align}
S'_{i,j}\left(x_1,\cdots,x_d\right)+T'_{i,j}\left(x_1\cdots,x_d\right)&=T'_{i,j-1}\left(x_1,\cdots,x_d\right)\\
S'_{i,j}\left(x_1,\cdots,x_d\right)-T'_{i,j}\left(x_1\cdots,x_d\right)&=T'_{i,j-1}\left(x_1,\cdots,-x_{d-i-j+1},\cdots,x_d\right)
\end{align}$$

which gives us

$$\begin{equation}
T'_{i,j}\left(x_1,\cdots,x_d\right)=\frac{1}{2}T'_{i,j}\left(x_1,\cdots,x_d\right)-T'_{i,j}\left(x_1\cdots,-x_{d-i-j+1},\cdots,x_d\right)
\end{equation}$$

which finally yields

$$\begin{equation}
T'_{i,d-i}=\frac{1}{2^{d-i}}\sum_{\ell\in\{0, 1\}^{d-i}}(-1)^{h(\ell)}T'_{i, 0}\left((-1)^{\ell_1}x_1,\cdots,(-1)^{\ell_{d-i}}x_{d-i},x_{d-i+1},\cdots,x_d\right)
\end{equation}$$

with $h$ being the Hamming weight. Putting everything together, we have

$$\begin{align}
\lambda_{d, t, 2k+b} &= \frac{1}{d^t}T'_{d-2k-b,2k+b}\\
\lambda_{d, t, 2k+b} &= \frac{1}{d^t2^{2k+b}}\sum_{\ell\in\{0, 1\}^{2k+b}}(-1)^{h(\ell)}T'_{d-2k-b, 0}\left((-1)^{\ell_1},\cdots,(-1)^{\ell_{d-2k-b}},1,\cdots,1\right)\\
\lambda_{d, t, 2k+b} &= \frac{1}{d^t2^{2k+b}}\sum_{\ell\in\{0, 1\}^{2k+b}}(-1)^{h(\ell)}S_{d-2k-b}\left((-1)^{\ell_1},\cdots,(-1)^{\ell_{d-2k-b}},1,\cdots,1\right)\\
\lambda_{d, t, 2k+b} &= \frac{1}{d^t2^{d}}\sum_{\ell\in\{0, 1\}^{2k+b}}(-1)^{h(\ell)}\sum_{j\in\{0, 1\}^{d-2k-b}}S_{0}\left((-1)^{\ell_1},\cdots,(-1)^{\ell_{d-2k-b}},(-1)^{j_1},\cdots,(-1)^{j_{d-2k-b}}\right)\\
\lambda_{d, t, 2k+b} &= \frac{1}{d^t2^{d}}\sum_{\ell\in\{0, 1\}^{2k+b}}(-1)^{h(\ell)}\sum_{j\in\{0, 1\}^{d-2k-b}}(2k+b-2h(\ell)+d-2k-b-2h(j))^t\\
\lambda_{d, t, 2k+b} &= \frac{1}{d^t2^{d}}\sum_{\ell\in\{0, 1\}^{2k+b}}(-1)^{h(\ell)}\sum_{j\in\{0, 1\}^{d-2k-b}}(d-2h(\ell)-2h(j))^t\\
\lambda_{d, t, 2k+b} &= \frac{1}{d^t2^{d}}\sum_{\ell\in\{0, 1\}^{2k+b}}(-1)^{h(\ell)}\sum_{j=0}^{d-2k-b}\binom{d-2k-b}{j}(d-2h(\ell)-2j)^t
\end{align}$$

which finally gives us

$$\begin{equation}
\label{eq:eigvalbin}
\lambda_{d, t, 2k+b} = \frac{1}{d^t2^{d}}\sum_{\ell=0}^{2k+b}(-1)^{\ell}\binom{2k+b}{\ell}\sum_{j=0}^{d-2k-b}\binom{d-2k-b}{j}(d-2\ell-2j)^t\,.
\end{equation}$$

Though this is an improvement over the initial expression, it's still quite ugly. Unfortunately, we don't have much hope to simplify this further. Indeed, suppose $t$ is even and we consider $k=0$. $\lambda_{d, t, 0}$ is then equal to $\left(\frac{2}{d}\right)^t\mathbb{E}\left[\left(X-\mathbb{E}[X]\right)^t\right]$, with $X\sim B\left(d,\frac12\right)$, and there is no (known?) closed form expression for the $t$-th centered moment of the binomial distribution, even if its second parameter is $\frac12$.

One other eigenvalue will be of interest however, namely the lowest positive one, $\lambda_{d, t, t}$. In this case, we can see using the original expression of the eigenvalue that if $t\leqslant d$, then $\lambda_{d, t, t}=\frac{t!}{d^t}$. More generally, note that a lower $k$ is associated to a *larger* eigenvalue.

Finally, note that this eigenvalue is associated to any equivalence class having $2k+b$ elements having an odd cardinality. In particular, its multiplicity is $\binom{d}{2k+b}$, since we have to choose the $2k+b$ elements of $[d]$ which have an odd cardinality.

### Computing the trace distance
Now that we have the eigenvalues, we are *technically* able to compute the trace distance between $\rho_{d, t, 2}$ and $\Pi_{d, t}$, since they commute, and are thus diagonal in the same basis. However, the eigenvalues of $\rho_{d, t, 2}$ having such an horrible expression, it doesn't seem easy to compute the trace distance.

However, as it turns out, there's a neat simplification in the regime $t\leqslant d$. Note that the rank of $\rho_{d, t, 2}$ is

$$\begin{equation}\mathrm{rk}\left(\rho_{d, t, 2}\right)=\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\binom{d}{2k+b}=\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\binom{d}{t-2k}\end{equation}$$

while the rank of $\Pi_{d, t}$ is $\binom{d+t-1}{t}$. In particular, in the common subspace where they're defined, $\rho_{d, t}$ is not full-rank, meaning that its lowest eigenvalue is $0$. As we've seen earlier, its lowest *positive* eigenvalue is $\frac{t!}{d^t}$.

Since $\rho_{d, t, 2}$ and $\Pi_{d, t}$ commute, we only have to care about the subspaces where the eigenvalues of $\rho_{d, t, 2}$ are lower than that of $\Pi_{d, t}$. What this means is that if

$$\begin{equation}\label{eq:conditionbin}\frac{t!}{d^t}\geqslant\frac{1}{\binom{d+t-1}{t}}\end{equation}$$

holds, then the only eigenvalue of $\rho_{d,t,2}$ that is lower than that of $\rho_{d, t}$ on the same subspace is $0$, in which case the trace distance between the two would be given by

$$\begin{equation}\frac12\\\|\rho_{d,t,2}-\Pi_{d, t}\\\|_1=\frac{\mathrm{rk}\left(\Pi_{d, t}\right)-\mathrm{rk}\left(\rho_{d, t, 2}\right)}{\binom{d+t-1}{t}}\,.\end{equation}$$

Thus, the question becomes: when does Equation \eqref{eq:conditionbin} holds? Well, the good news is: it always does! Indeed, this equation is equivalent to

$$\begin{equation}\frac{(d+t-1)!}{(d-1)!}\geqslant d^t\,.\end{equation}$$

By rewriting the LHS term as $\prod\limits_{i=d}^{d+t-1}i$, we can lower bound each of the termis by $d$, yielding the inequality. This allows us to conclude that

$$\begin{equation}\boxed{\frac12\\\|\rho_{d,t,2}-\Pi_{d, t}\\\|_1=1 - \frac{1}{\binom{d+t-1}{t}}\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\binom{d}{t-2k}}\end{equation}$$

for all $d$ and $t\leqslant d$. Though exact, this expression isn't the most convenient to work with, so let us write down some of its asymptotics depending on the value of $t$.

First of all, note that we have

$$\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\binom{d}{t-2k}=\binom{d}{t}\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\frac{\binom{d}{t-2k}}{\binom{d}{t}}\,.$$

Now, if $t=o(d)$, we have

$$\begin{equation}\frac{\binom{d}{t-2k}}{\binom{d}{t}}=\left(\frac{t}{d}\right)^{2k}+o\left(\left(\frac{t}{d}\right)^{2k}\right)\,.\end{equation}$$

This translates the relatively intuitive idea that since $t=o(d)$, we asymptotically have $t\leqslant\frac{d}{2}$, meaning that the terms with low $k$ dominate the other ones. Thus, we have

$$\begin{equation}\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\binom{d}{t-2k}=\binom{d}{t}\left(1+\frac{t^2}{d^2}+o\left(\frac{t^2}{d^2}\right)\right)\,.\end{equation}$$

We are thus left with determining the asymptotics for $\frac{\binom{d}{t}}{\binom{d+t-1}{t}}=\frac{d!(d-1)!}{(d-t)!(d+t-1)!}$, which we can get using Equations \eqref{eq:asymptoticsproduct1} and \eqref{eq:asymptoticsproduct2}, giving us

$$\begin{equation}\frac{\binom{d}{t}}{\binom{d+t-1}{t}}=\frac{d^{t-1}-\frac{t(t-1)}{2}d^{t-2}+\Theta\!\left(t^4d^{t-3}\right)}{d^{t-1}+\frac{t(t-1)}{2}d^{t-2}+\Theta\!\left(t^4d^{t-3}\right)}\end{equation}$$

which we can simplify as

$$\begin{equation}\frac{\binom{d}{t}}{\binom{d+t-1}{t}}=1-\frac{t(t-1)}{d}+\Theta\!\left(\frac{t^4}{d^2}\right)\,.\end{equation}$$

Thus, we can finally write

$$\begin{align}
\frac12\|\rho_{d,t,2}-\Pi_{d, t}\|_1&=1 - \frac{1}{\binom{d+t-1}{t}}\sum_{k=0}^{\left\lfloor\frac{t}{2}\right\rfloor}\binom{d}{t-2k}\\
&=1 - \frac{\binom{d}{t}}{\binom{d+t-1}{t}}\left(1+\frac{t^2}{d^2}+o\left(\frac{t^2}{d^2}\right)\right)\\
&= 1 - \left(1-\frac{t(t-1)}{d}+\Theta\!\left(\frac{t^4}{d^2}\right)\right)\left(1+\frac{t^2}{d^2}+o\left(\frac{t^2}{d^2}\right)\right)\\
&= \boxed{\frac{t(t-1)}{d}+\Theta\!\left(\frac{t^4}{d^2}\right)}\,.
\end{align}$$

In order for our approximation to be useful, we thus have to consider $t=o\left(\sqrt{d}\right)$. All in all, we can see that we saved a factor $\frac32$ in the dominant term $\frac{t^2}{d}$ with respect to Brakerski and Shmueli's and Ananth, Gulati, Qian and Yuen's bounds.

If $t\sim\alpha\sqrt{d}$ on the other hand, then Stirling's approximation gives us

$$\begin{equation}\frac{d!(d-1)!}{(d-t)!(d+t-1)!}\sim\frac{\sqrt{2\pi d}\left(\frac{d}{\mathrm{e}}\right)^d\sqrt{2\pi(d-1)}\left(\frac{d-1}{\mathrm{e}}\right)^{d-1}}{\sqrt{2\pi(d-t)}\left(\frac{d-t}{\mathrm{e}}\right)^{d-t}\sqrt{2\pi(d+t-1)}\left(\frac{d+t-1}{\mathrm{e}}\right)^{d+t-1}}\,.\end{equation}$$

We can simplify this to

$$\begin{equation}\frac{d!(d-1)!}{(d-t)!(d+t-1)!}\sim\frac{d^d(d-1)^{d-1}}{(d-t)^{d-t}(d+t-1)^{d+t-1}}\,.\end{equation}$$

Now note that we have

$$\begin{equation}\ln\left(\frac{d^d}{(d-t)^{d-t}}\right)=t\ln(d)+t-\frac{\alpha^2}{2}+o(1)\end{equation}$$

and

$$\begin{equation}\ln\left(\frac{(d-1)^{d-1}}{(d+t-1)^{d+t-1}}\right)=-t\ln(d)-t-\frac{\alpha^2}{2}+o(1)\end{equation}$$

which gives us

$$\begin{equation}\frac12\|\rho_{d,t,2}-\Pi_{d, t}\|_1=\boxed{1-\mathrm{e}^{-\alpha^2}+o(1)}\,.\end{equation}$$
## A quick note on the other phase states
Now, what about the general case, for an arbitrary $P$? Well, first of all, we can note that for all $P\geqslant t$, $\rho_{d,t,P}=\rho_{d, t, t}$. So, let us restrict ourselves to $P\leqslant t$.

A quick computation shows that $\rho_{d, t, P}$ can still be written as in Equation \eqref{eq:density-matrix-equivalence}. Indeed, we have

$$\begin{equation}\rho_{d, t, P}=\frac{1}{d^t}\sum_{x\sim y}\ketbra{x}{y}\end{equation}$$

with $\sim$ being the equivalence relation defined as

$$\begin{equation}x\sim y\iff \forall i\in[d],n_i(x)=n_i(y)\pmod{P}\end{equation}$$

with $n_i(x)$ being the number of times $i$ appears in $x\in[d]^t$. We are interested in the lowest positive eigenvalue of $\rho_{d, t, P}$. The associated equivalence class will be the one for which $0$ appears $P-1$ times, $1$ appears $P-1$ times, up until $\left\lfloor\frac{t}{P-1}\right\rfloor-1$ appears $P-1$ times, with $\left\lfloor\frac{t}{P-1}\right\rfloor$ appearing $t-(P-1)\left\lfloor\frac{t}{P-1}\right\rfloor$ times. This results in the eigenvalue being

$$\begin{equation}\frac{t!}{d^t[(P-1)!]^{\left\lfloor\frac{t}{P-1}\right\rfloor}\left(t-(P-1)\left\lfloor\frac{t}{P-1}\right\rfloor\right)!}\,.\end{equation}$$

If we write $t=q(P-1)+r$ the euclidean division of $t$ by $P-1$, then this eigenvalue can simply be written as

$$\begin{equation}\frac{t!}{d^t[(P-1)!]^qr!}\,.\end{equation}$$

Note that this lowest positive eigenvalue is lower than that of $\rho_{d, t, 2}$, so that the regimes in which it is larger than $\frac{1}{\binom{d+t-1}{t}}$ is more restricted, and we might have to consider more subspaces to compute the trace distance than only the one in which $\rho_{d, t, P}$ is nil.

## Cite this blog post
```bibtex
@online{NemozBlogPost|{{ page.name | truncate: 15, "" }},
  author={Tristan Nemoz},
  title={% raw %}{{% endraw %}{{ page.title }}{% raw %}}{% endraw %},
  date={% raw %}{{% endraw %}{{ page.last_modified_at | date: '%Y-%m-%d' }}{% raw %}}{% endraw %},
  url={% raw %}{{% endraw %}{{ page.url | absolute_url }}{% raw %}}{% endraw %},
  urldate={% raw %}{{% endraw %}DATE_TO_BE_REPLACED{% raw %}}{% endraw %}
}
```
<script>
    const date = new Date();
    var s_class_elts = document.getElementsByClassName("s");
    for (var i = 0; i < s_class_elts.length; i++) {
        if (s_class_elts[i].innerText == "{DATE_TO_BE_REPLACED}") {
            s_class_elts[i].innerText = "{" + date.toISOString().split("T")[0] + "}";
        }
    }
</script>
