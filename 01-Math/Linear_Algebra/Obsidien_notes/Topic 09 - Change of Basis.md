# Topic 09 — Change of Basis

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

## 📌 Summary
Change of basis is like speaking in another language — it's a matrix whose columns represent the change of basis vectors, thought of as a transformation that moves our basis vectors.

---

## 🧠 Core Idea

> It's like **speaking in another language**.

A matrix whose **columns represent the change of basis vectors** can be thought of as a transformation that moves our basis vectors.

→ We need to **inverse the vectors** (new basis) $\begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$ — the inverse transformation is a new transformation.

---

## 📐 To Translate a Matrix

$$\underbrace{\begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}}_{\text{Inverse change of basis}} \underbrace{\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}}_{\text{Transformation matrix in our language}} \underbrace{\begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}^{-1}}_{\text{Change of basis matrix}} \underbrace{\begin{bmatrix} -1 \\ 2 \end{bmatrix}}_{\text{Start with any vector}}$$

→ Result: **Transformed vector in our language**

---

## 🔗 Related Topics
- [[Topic 08 — Cramer's Rule]]
- [[Topic 10 — Eigenvectors and Eigenvalues]]

---

*Tags: #linear-algebra #change-of-basis #math #phase-1*
