# Topic 01 — Vectors

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

# Summary
A vector is an arrow in space defined by its length and direction. It can be viewed from three perspectives: Physics, CS, and Math.

---

# Perspectives on Vectors

# Physics Perspective
- Vectors are arrows pointing in space
- Defined by a given vector's **length** and the **direction** it's pointing
- Can be two-dimensional or three-dimensional

# CS Perspective
- Vectors are **ordered lists of numbers**

# Math Perspective
- A vector can be anything where there's a sensible notion of **adding two vectors** and **multiplying a vector by a number**

---

# Definition
> A vector is an arrow inside a coordinate system, like the xy-plane, with its **tail at the origin**.

$$\vec{v} = \begin{bmatrix} -2 \\ 3 \end{bmatrix} \quad \begin{bmatrix} -2 \\ -4 \\ y \end{bmatrix}$$

---

# Vector Addition
To add two vectors, move one from its origin so the result is the sum of both vectors.

$$\vec{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 1+3 \\ 2+(-1) \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$$

---

# Vector Multiplication (Scaling)
Multiplying a vector by a number will **increase or reduce the length** of the vector.
- This is called **"Scaling"**
- The numbers are called **"Scalars"**

---

## 🧭 Basis Vectors
- Noted $\hat{i}$ and $\hat{j}$ of the xy coordinate system
- Any vector is a **linear combination** of basis vectors:

$$a\vec{v} + b\vec{w}$$

---

## 🌐 The Span
> The span of $\vec{v}$ and $\vec{w}$ is the **set of all their linear combinations** $a\vec{v} + b\vec{w}$

For 3D:
$$a\vec{v} + b\vec{w} + c\vec{u}$$
(let these constants vary)

### Linearly Dependent
$$\vec{v} = a\vec{v} + b\vec{w}$$
→ One is a scaled version of the other (for some values of a and b)

### Linearly Independent
$$\vec{v} \neq a\vec{v} + b\vec{w}$$
(for all values of a and b)

---

# Technical Definition of Basis
> The basis of a vector space is a set of **linearly independent** vectors that **span** the full space.

**Note:** A vector is a linear combination of the basis vectors.

---

# Related Topics
- [[Topic 02 — Matrices]]
- [[Topic 03 — Determinant]]

---

*Tags: #linear-algebra #vectors #math #phase-1*
