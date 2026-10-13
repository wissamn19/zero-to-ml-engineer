# Topic 12 — Norms

**Subject:** Linear Algebra for ML
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

# Summary
A vector norm maps a vector to a **scalar** that measures how "big" the vector is. Different rules give different norms: $L^1$, $L^2$, $L^3$, $L^\infty$, and the general $L^p$.

---

# Why Norms?

Taking two vectors, one is $a = \begin{bmatrix} 3 \\ -4 \end{bmatrix}$ and the other one is $b = \begin{bmatrix} 0 \\ 5 \end{bmatrix}$, but we want to know **which one is bigger**:

→ here we use **norms** (vector norm).

## 1. Vector Norm
> A vector norm gives us a way to **measure how "big" a vector is**.

- Maps a vector to a **scalar** based on a specific rule.

---

# Rules

$$\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} \xrightarrow[L^1 \text{ Norm}]{|a_1| + |a_2| + \dots + |a_n|} \|a\|_1 \rightarrow \text{scalar}$$

$$\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} \xrightarrow[L^2 \text{ Norm}]{\sqrt{a_1^2 + a_2^2 + \dots + a_n^2}} \|a\|_2$$

$$\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} \xrightarrow[L^3 \text{ Norm}]{\sqrt[3]{|a_1|^3 + |a_2|^3 + \dots + |a_n|^3}} \|a\|_3$$

Then we can use the scalars to measure how "big" vectors are.

---

# $L^1$ Norm

> **Adds up the absolute values** of a vector's components.

$$\|a\|_1 = 3 + |-4| = 7$$

$$\|b\|_1 = 0 + 5 = 5$$

$$\|a\|_1 > \|b\|_1$$

→ So according to the $L^1$ norm, the first vector $a$ is **larger**.

- Its contours are **diamonds**.

---

# $L^2$ Norm

> Comes from the **Pythagorean theorem**.

- **Square** each component, **add** them up, and take the **square root**.

$$\|a\|_2 = \sqrt{3^2 + (-4)^2} = 5$$

$$\|b\|_2 = \sqrt{0^2 + 5^2} = 5$$

$$\|a\|_2 = \|b\|_2$$

- Its contours are **perfect circles**.

---

# $L^3$ Norm

$$\|a\|_3 = \sqrt[3]{|a_1|^3 + |a_2|^3 + \dots + |a_n|^3}$$

---

# $L^\infty$ Norm

$$\|a\|_\infty = \max\{|x_1|, |x_2|\}$$

$$a = \begin{bmatrix} 3 \\ -4 \end{bmatrix} \Rightarrow \|a\|_\infty = \max\{3, |-4|\} = 4$$

$$b = \begin{bmatrix} 0 \\ 5 \end{bmatrix} \Rightarrow \|b\|_\infty = \max\{0, 5\} = 5$$

---

# $L^p$ Norm

$$\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} \longrightarrow \left(|a_1|^p + |a_2|^p + \dots + |a_n|^p\right)^{1/p} = \|a\|_p$$

> **Increase $p$** to get the **square** ($\square$) shape.

---

# Geometric View

![[norm-contours.png]]

Each shape = all vectors with norm $5$, for $a = (3, -4)$ and $b = (0, 5)$. Inside the shape = smaller than 5, outside = bigger.

- $p = 1$ → diamond, $p = 2$ → circle, $p \to \infty$ → square.
- $a$ is bigger than $b$ under $L^1$, equal under $L^2$, and smaller under $L^3$ and $L^\infty$.

---

## Related Topics
- [[Topic 11 — SVD]]
- [[Topic 02 — Matrices]]

---

*Tags: #linear-algebra #norms #vector-norm #math #phase-1*