# Topic 11 — SVD (Singular Value Decomposition)

**Subject:** Linear Algebra for ML
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

# Summary
SVD decomposes any matrix (any shape) into three matrices: $U$, $\Sigma$, $V^T$. It can also be written as a sum of rank-one layers sorted by importance. The more layers we keep, the better the approximation of $X$.

---

## 1. SVD
> The process of **decomposing a matrix (any shape)** into the **product of three other matrices**.

$$X = U \Sigma V^T$$

- $X = \begin{bmatrix} | & | & & | \\ x_1 & x_2 & \cdots & x_m \\ | & | & & | \end{bmatrix}$ = data matrix, with $n \gg m$
- $x_k \in \mathbb{R}^n$ (dimension)
- $U$, $V$ = **unitary matrices** (orthogonal matrices)
- $\Sigma$ = **diagonal matrix**

---

# Expanded Form

$$X = \begin{bmatrix} | & | & & | \\ u_1 & u_2 & \cdots & u_m \\ | & | & & | \end{bmatrix} \begin{bmatrix} \sigma_1 & & \\ & \ddots & \\ & & \sigma_m \\ & 0 & \end{bmatrix} \begin{bmatrix} v_1 & v_2 & \cdots & v_m \end{bmatrix}^T$$

- $U$ columns → **"eigen" faces**
- $\Sigma$ → **ordered by importance**
- $V$ → **"eigen" time series**

---

# Unitary Matrices

$U, V$ = unitary matrices

$$UU^T = U^TU = I_{n \times n} \quad \text{(transpose)}$$

$$VV^T = V^TV = I_{m \times m}$$

> $V$ has the same property as $U$.

---

# Naming the Matrices

Singular values are ordered:

$$\sigma_1 \geq \sigma_2 \geq \sigma_3 \geq \dots \geq \sigma_m \geq 0$$

So we call each of these matrices like so:

$$U \quad \Sigma \quad V^T$$

- $U$ = **left singular vectors**
- $\Sigma$ = **singular values**
- $V$ = **right singular vectors**

---

# Geometric View

![[svd-geometry.gif]]

SVD = **rotate → stretch → rotate**, applied to the unit circle:

1. $V^T$ → **rotate** ($v_1, v_2$ land on the axes)
2. $\Sigma$ → **stretch** by $\sigma_1$ and $\sigma_2$ along the axes (circle → ellipse)
3. $U$ → **rotate** again (the axes land on $u_1, u_2$)

---

# Interpretation of Components

- $U$ columns have the **same shape as $X$**, so they can be reshaped (e.g. back into images).
- $V^T$ rows → **mixtures of all values to take the $x$'s**:

$$V^T = \begin{bmatrix} - & v_1^T & - \\ - & v_2^T & - \\ & \vdots & \\ - & v_m^T & - \end{bmatrix}$$

---

# Sum of Rank-One Matrices

$$X = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T + \dots + \sigma_m u_m v_m^T + 0$$

$$X = U \Sigma V^T = \hat{U} \hat{\Sigma} V^T \quad \rightarrow \text{Economy SVD}$$

Each term is a column ($u_i$) times a row ($v_i^T$), scaled by $\sigma_i$:

$$X = \sigma_1 \underbrace{u_1}_{\text{column}} \underbrace{v_1^T}_{\text{row}} + \sigma_2 u_2 v_2^T + \dots + \underbrace{\sigma_r u_r v_r^T}_{\text{truncate at } r} + \dots + \sigma_m u_m v_m^T + 0$$

- These rank-one matrices are **layers that increasingly improve the approximation of $X$**.
- So each $\sigma_i u_i v_i^T$ is a **simple image**, and the layers are **sorted by importance** ($\sigma_1, \sigma_2, \dots$).

---

# Why More "Rank-One Matrices" Gives a Better Image?

- **Layer 1** (biggest $\sigma$): captures the broad structure: overall light and dark regions.
- **Layers 2 to 20**: add the main shapes and edges.
- **Later layers**: add finer and finer detail.
- **The last layers**: have tiny $\sigma$ and mostly add noise and texture.

---

# The Eckart–Young Theorem (1936)

> The **best approximation** to the matrix $X$ that has rank $r$.

$$\underset{\tilde{X}\ \text{such that}\ \text{rank}(\tilde{X}) = r}{\arg\min} \|X - \tilde{X}\|_F = \tilde{U} \tilde{\Sigma} \tilde{V}^T$$

- $\arg\min$ → **smallest error**
- $F$ → **Frobenius norm**

→ So the theorem **guarantees** that the best possible matrix approximation to $X$ of rank $r$ is the **first $r$ layers**.

---

# Unitary Identity After Truncation

$$\tilde{U}^T \tilde{U} = I_{r \times r}$$

$$\tilde{U} \tilde{U}^T \neq I$$

> It's not an identity anymore.

---

## Related Topics
- [[Topic 10 — Eigenvectors and Eigenvalues]]
- [[Topic 09 — Change of Basis]]

---

*Tags: #linear-algebra #svd #matrix-decomposition #eckart-young #math #phase-1*