# PCA from scratch
---

Implementation of Principal Component Analysis (PCA) built from first principles using NumPy, no `sklearn.decomposition.PCA` used for the algorithm itself (only for loading the Iris dataset).

## What it does

Reduces the 4-dimensional Iris dataset (sepal length/width, petal length/width) down to 2 dimensions while preserving as much variance as possible, then visualizes the result.

## How it works

1. **Center the data**: subtract the mean of each feature so the data is centered at the origin.
2. **Compute the covariance matrix**: a 4x4 matrix describing how each pair of features varies together.
3. **Eigen decomposition**: find the eigenvectors and eigenvalues of the covariance matrix. Eigenvectors = directions of variance in the data; eigenvalues = how much variance lies along each direction.
4. **Sort and select**: sort eigenvectors by eigenvalue, descending. Keep the top 2 (the "principal components").
5. **Project**: matrix-multiply the centered data by the selected eigenvectors to get each flower's coordinates in the new 2D space.
6. **Plot**: scatter the projected points, colored by species.

## Result

PC1 alone separates *setosa* cleanly from the other two species. *Versicolor* and *virginica* overlap partially on PC1/PC2, since their distinguishing information is spread across directions not captured by just 2 components.

## Usage

\```bash
python pca.py
\```

## What I learned

- Why centering matters before computing covariance
- How eigenvectors/eigenvalues of a covariance matrix relate to directions and magnitude of variance
- That projection is just a dot product, measuring how far each point lies along each new axis
- `np.cov` expects features as rows by default (`rowvar=True`). either transpose the data or pass `rowvar=False`