# Topic 04 — Linear System of Equations

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

# Summary
One of the core uses of matrices is to solve systems of equations. This reduces to finding the inverse matrix $A^{-1}$ such that $A\vec{x} = \vec{v}$.

---

## 1. System of Equations

One of the usefulness of matrices is to **solve systems of equations**.

Example:
$$6x - 3y + 2z = 7$$
$$x + 2y + 5z = 0$$
$$2x - 8y - z = -2$$

Which is:
$$\underbrace{\begin{bmatrix} 6 & -3 & 2 \\ 1 & 2 & 5 \\ 2 & -8 & -1 \end{bmatrix}}_{A} \underbrace{\begin{bmatrix} x \\ y \\ z \end{bmatrix}}_{\vec{x}} = \underbrace{\begin{bmatrix} 7 \\ 0 \\ -2 \end{bmatrix}}_{\vec{v}}$$

So now we have:
$$A\vec{x} = \vec{v}$$

---

## 2. Inverse Matrix — $A^{-1}$

> $A^{-1}$ is a unique transformation with the property that if you first apply $A$ then $A^{-1}$, you end up right where you started. $(A A^{-1})$ — this is called the **identity transformation**.

$$A^{-1}A\vec{x} = A^{-1}\vec{v} \Rightarrow \text{The "do nothing" matrix}$$

- If $\det(A) \neq 0 \Rightarrow A^{-1}$ exists
- If $\det(A) = 0 \Rightarrow$ No $A^{-1}$

---

## 3. Rank

> When the output of a transformation is a **line**, the transformation has a **rank of one**.

- For two-dimensional plane → rank of two
- The rank = the **number of dimensions in the output** of the transformation (column space)

---

## 4. Column Space

> The set of **all possible outputs** of the matrix — it calls column space.

---

## 5. Null Space or "Kernel"

> The space of **all vectors that become null** (zero vector) after the transformation.

---

## Related Topics
- [[Topic 02 — Matrices]]
- [[Topic 03 — Determinant]]
- [[Topic 05 — Non-Square Matrix as Transformation]]

---

*Tags: #linear-algebra #systems-of-equations #inverse-matrix #rank #math #phase-1*
