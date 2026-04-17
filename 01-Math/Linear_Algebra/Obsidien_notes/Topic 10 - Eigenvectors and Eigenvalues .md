# Topic 10 — Eigenvectors and Eigenvalues

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

# Summary
Eigenvectors are special vectors that stay on their own span after a linear transformation. Eigenvalues are the factor by which they get stretched or squished.

---

## 1. Eigenvectors
> Any vector where its **span stays the same** after the linear transformation.

## 2. Eigenvalues
> Which is just the **factor by which it's stretched or squished** during the linear transformation.

---

# Symbolically

$$A\vec{v} = \lambda\vec{v} \quad \rightarrow \text{Eigenvalue}$$

- $A$ = transformation matrix (matrix-vector multiplication)
- $\vec{v}$ = eigenvector
- $\lambda$ = eigenvalue (scalar)

> It says that the **matrix-vector multiplication** gives the same result as just **scaling the eigenvector** $\vec{v}$ by some value $\lambda$.

---

# Seeking Eigenvalue $\lambda$

$$A\vec{v} = \lambda\vec{v}$$
$$A\vec{v} - \lambda I\vec{v} = 0$$
$$(A - \lambda I)\vec{v} = 0$$
$$\det(A - \lambda I) = 0$$

Matrix multiplication by $\lambda$:

$$\begin{bmatrix} \lambda & 0 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda \end{bmatrix} \Rightarrow \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

We want a **non-zero solution** for $\vec{v}$:
- "Squishification" → $\det(A - \lambda I) = 0$
- This matrix will look like: $\begin{bmatrix} 3-\lambda & 1 & 4 \\ 1 & 5-\lambda & 9 \\ 2 & 6 & 5-\lambda \end{bmatrix}$

→ So the $\lambda$ value should be 1, which means this value will remain the vector to be a line.

### Steps:
1. $A\vec{v} = \lambda\vec{v}$
2. $A\vec{v} - \lambda I\vec{v} = 0$
3. $(A - \lambda I)\vec{v} = 0$
4. $\det(A - \lambda I) = 0$

### Example:
$$\det\left(\begin{bmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{bmatrix}\right) = (3-\lambda)(2-\lambda) - 0 \cdot 1$$

This is a **quadratic polynomial in $\lambda$**.

$$(3-\lambda)(2-\lambda) = 0$$
$$\lambda = 3 \quad \text{or} \quad \lambda = 2$$

**Note:** Some vectors don't have an eigenvalue (e.g. 90° rotation).

---

# Or Complex Numbers

$$\det\left(\begin{bmatrix} -\lambda & 1 \\ 1 & -\lambda \end{bmatrix}\right) = (-\lambda)(-\lambda) - 1 = \lambda^2 - 1 = 0$$
$$\lambda = i \quad \text{or} \quad \lambda = -i$$

---

# Eigenbasis
> It's the same concept for the **change of basis**.

We use our eigenvectors as basis (new one) — **Diagonal**:

$$\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}^{-1} \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}$$

→ Change of basis matrix

---

## 📊 Some Facts to Know

**1) Trace:**
$$\text{Tr}\left(\begin{bmatrix} a & b \\ c & d \end{bmatrix}\right) = a + d = \lambda_1 + \lambda_2$$
$$\frac{1}{2}\text{Tr}\left(\begin{bmatrix} a & b \\ c & d \end{bmatrix}\right) = \frac{a+d}{2} = \frac{\lambda_1 + \lambda_2}{2}$$
$$\text{mean}(a,d) = \text{mean}(\lambda_1, \lambda_2)$$

**2) Determinant:**
$$\det\left(\begin{bmatrix} a & b \\ c & d \end{bmatrix}\right) = ad - bc = \lambda_1 \lambda_2$$

**3) Eigenvalue shortcut:**
$$\lambda_1, \lambda_2 = m \pm \sqrt{m^2 - p}$$

where $m$ = mean of diagonal, $p$ = product (determinant).

---

# inding Eigenvalues — Example

We call the mean $(m)$ which is the trace, and the det as $(p)$ for product.

**Find the distance:**
$$\begin{bmatrix} 8 & 4 \\ 2 & 6 \end{bmatrix} \quad m = 7, \quad p = 40$$

$$40 = (7-d)(7+d)$$
$$40 = 7^2 - d^2$$
$$d^2 = 7^2 - 40 \Rightarrow d^2 = 9 \Rightarrow d = 3$$

So $\lambda_1 = -3+7 = 4$, $\lambda_2 = 3+7 = 10$ ... wait:
$$\lambda_{1,2} = m \pm d = 7 \pm 3 \Rightarrow \lambda_1 = 4, \quad \lambda_2 = 10$$

**General formula:**
$$d^2 = m^2 - p \quad \Rightarrow \quad \lambda_{1,2} = m \pm \sqrt{m^2 - p}$$

**Example:** $x^2 - 10x + 9 = 5$, so $x^2 - 10x + 9$:
- Mean = 5
- $(x - \lambda_1)(x - \lambda_2)$
- $x^2 - (\lambda_1 + \lambda_2)x + \lambda_1\lambda_2$ → m (sum), product

---

# Find the Eigenvalues of $\begin{bmatrix} 3 & 1 \\ 4 & 1 \end{bmatrix}$

$$\det\left(\begin{bmatrix} 3-\lambda & 1 \\ 4 & 1-\lambda \end{bmatrix}\right) = (3-\lambda)(1-\lambda) - 4(1)$$
$$= (3 - 3\lambda - \lambda + \lambda^2) - 4$$
$$= (3 - 4\lambda + \lambda^2) - 4$$
$$= \lambda^2 - 4\lambda - 1 = 0$$

$$\lambda_{1,2} = \frac{4 \pm \sqrt{4^2 - 4(1)(-1)}}{2} = \frac{4 \pm \sqrt{20}}{2} = 2 \pm \sqrt{5}$$

---

## Related Topics
- [[Topic 09 — Change of Basis]]
- [[Topic 02 — Matrices]]

---

*Tags: #linear-algebra #eigenvectors #eigenvalues #eigenbasis #math #phase-1*
