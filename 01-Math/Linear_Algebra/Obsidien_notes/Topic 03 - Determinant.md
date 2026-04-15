# Topic 03 — Determinant

**Subject:** Linear Algebra for ML (3Blue1Brown)
**Status:** #status/growing
**MOC:** [[MOC - Math]]

---

## 📌 Summary
The determinant measures **how much a linear transformation scales areas**. It can be negative (flipping orientation) and zero means the transformation squishes space into a lower dimension.

---

## 🧠 Core Idea

- *How much are areas scaled?*
- The linear transformation scales its area
- The special scaling factor by which a linear transformation changes any area is called the **determinant**

---

## 📐 Formula

### 2×2 Matrix:
$$\det\left(\begin{bmatrix} a & b \\ c & d \end{bmatrix}\right) = ad - bc$$

### 3×3 Matrix:
$$\det\left(\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}\right) = a \det\begin{bmatrix} e & f \\ h & i \end{bmatrix} - b \det\begin{bmatrix} d & f \\ g & i \end{bmatrix} + c \det\begin{bmatrix} d & e \\ g & h \end{bmatrix}$$

---

## ⚠️ Notes
- The determinant **can be negative** because of the scaling (flipping orientation)
- **Question:** $\det(M_1 M_2) = \det(M_1) \cdot \det(M_2)$
  - → Applying two transformations in sequence multiplies their area-scaling factors
  - → The determinant is that scaling factor

---

## 🔗 Related Topics
- [[Topic 02 — Matrices]]
- [[Topic 04 — Linear System of Equations]]

---

*Tags: #linear-algebra #determinant #math #phase-1*
