import numpy as np
import matplotlib.pyplot as plt
from skimage import data

img = data.camera().astype(float)
U, S, Vt = np.linalg.svd(img, full_matrices=False)

ks = [0, 5, 30, 70, 100]
fig, axes = plt.subplots(1, len(ks) + 1, figsize=(14, 4))

axes[0].imshow(img, cmap="gray")
axes[0].set_title("original")

for ax, k in zip(axes[1:], ks):
    approx = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    ax.imshow(approx, cmap="gray")
    ax.set_title(f"k={k}")

for ax in axes:
    ax.axis("off")
plt.show()