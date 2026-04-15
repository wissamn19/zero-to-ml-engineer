# Topic 07 — Cross Product

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

## 📌 Summary
The cross product of two 3D vectors gives a new 3D vector perpendicular to both, with magnitude equal to the area of the parallelogram they form.

---

## 🧠 Core Idea

The cross product between $\vec{v}$ and $\vec{w}$ is written as:

$$\vec{v} \times \vec{w} = \text{Area of parallelogram}$$
$$= -\vec{w} \times \vec{v}$$

- To compute it, we use the **determinant**:

$$\begin{bmatrix} 3 & 1 \\ 1 & -2 \end{bmatrix} = -(1 - (-6)) = -7$$

- More perpendicular → $\vec{v} \times \vec{w}$ is **Bigger**
- Similar direction → $\vec{v} \times \vec{w}$ is **Smaller**

$$(3\vec{v}) \times \vec{w} = 3(\vec{v} \times \vec{w})$$

---

## 1. Cross Product (Full Definition)

> Is a **vector** with a specific length — the result of combining two different 3D vectors to get a 3D vector ($\vec{v} \times \vec{w} = \vec{p}$)

$$\begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \times \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \det\begin{bmatrix} \hat{i} & v_1 & w_1 \\ \hat{j} & v_2 & w_2 \\ \hat{k} & v_3 & w_3 \end{bmatrix}$$

$$= \hat{i}(v_2 w_3 - v_3 w_2) + \hat{j}(v_3 w_1 - v_1 w_3) + \hat{k}(v_1 w_2 - v_2 w_1)$$

The result is **perpendicular to each other and still with unit lengths**.

---

## 📐 Area Formula

$$\text{Area} = \det(A) \cdot y$$

$$y = \frac{\text{Area}}{\det(A)} = \frac{\det\begin{bmatrix} y & -1 \\ 0 & 2 \end{bmatrix}}{\det\begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix}}$$

$$\text{Area} = 1 \times x, \quad x = \frac{\text{Area}}{\det(A)} = \frac{\det\begin{bmatrix} 2 & -1 \\ y & 2 \end{bmatrix}}{\det\begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix}} = \frac{(4)(1) - (2)(-1)}{(2)(4) - (0)(-1)} = \frac{6}{2} = 3$$

---

## 🔗 Related Topics
- [[Topic 06 — Dot Product and Duality]]
- [[Topic 08 — Cramer's Rule]]

---

*Tags: #linear-algebra #cross-product #math #phase-1*
