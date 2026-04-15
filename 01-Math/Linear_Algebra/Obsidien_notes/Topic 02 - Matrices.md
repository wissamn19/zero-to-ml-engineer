# Topic 02 — Matrices

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

## 📌 Summary
A matrix encodes a linear transformation. Matrix multiplication represents the composition of two transformations applied in sequence (read right to left).

---

## 1. Linear Transformation

> Transformation is a fancy word for **function** — it takes an input and spits an output.

### What makes it *Linear*? Two properties:
1. All lines must remain lines **without getting curved**
2. The **origin must remain fixed** in place

→ So Linear Transformation is **keeping grid lines parallel and evenly spaced**.

### How to describe one numerically?
- We need to record where the basis vectors $\hat{i}$ and $\hat{j}$ land
- To find where **any** vector lands, use:

$$\begin{bmatrix} x \\ y \end{bmatrix} \rightarrow x\begin{bmatrix} 1 \\ 0 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \end{bmatrix} \Rightarrow x\begin{bmatrix} 1 \\ -2 \end{bmatrix} + y\begin{bmatrix} 3 \\ 0 \end{bmatrix} = \begin{bmatrix} 1x+3y \\ -2x+0y \end{bmatrix}$$

- You can use a **2×2 matrix** for $\hat{i}$, $\hat{j}$:

$$\begin{bmatrix} a & 3 \\ -2 & 0 \end{bmatrix}$$

To find where a transformation takes vector $\begin{bmatrix} 5 \\ 7 \end{bmatrix}$, apply:

$$5\begin{bmatrix} 1 \\ -2 \end{bmatrix} + 7\begin{bmatrix} 3 \\ 0 \end{bmatrix}$$

---

### What is "Shear"?
> It's a kind of notation to the basis vectors (skewing the grid)

### What is "Composition"?
> Rotation and a shear combined.

To know where the vector ends up:

$$\underbrace{\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}}_{\text{Shear}} \left( \underbrace{\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}}_{\text{Rotation}} \begin{bmatrix} x \\ y \end{bmatrix} \right) = \underbrace{\begin{bmatrix} 1 & -1 \\ 1 & 0 \end{bmatrix}}_{\text{Composition}} \begin{bmatrix} x \\ y \end{bmatrix}$$

> Read **right to left**

---

## 2. Matrix Multiplication

To multiply M1 and M2:

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} e & f \\ g & h \end{bmatrix} = \begin{bmatrix} ae+bg & af+bh \\ ce+dg & ac+dh \end{bmatrix}$$

**Note:**
- $M_1 \cdot M_2 \neq M_2 \cdot M_1$ (not commutative)
- But: $(AB)C = A(BC)$ (associative ✅)

---

## 🔗 Related Topics
- [[Topic 01 — Vectors]]
- [[Topic 03 — Determinant]]
- [[Topic 04 — Linear System of Equations]]

---

*Tags: #linear-algebra #matrices #transformation #math #phase-1*
