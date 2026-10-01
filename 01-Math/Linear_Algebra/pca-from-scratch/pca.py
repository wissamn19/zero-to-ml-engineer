import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def load_data():
    iris = load_iris()
    x = iris.data
    y = iris.target
    return x,y

def center_data(x):
    mean = np.mean(x, axis=0)
    x_centered = x - mean
    return x_centered, mean

def compute_covariance(x_centered):
   x_centered = x_centered.T  
   cov_matrix = np.cov(x_centered)
   return cov_matrix

def eigen_decompose(cov_matrix):
    eigrnvals, eigvecs = np.linalg.eig(cov_matrix)
    return eigrnvals, eigvecs

def project(x_centered, eigenvectors, n_components=2):
   x_proj = np.dot(x_centered, eigenvectors[:, :n_components])
   return x_proj


def plot_projection(x_proj, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x_proj[:, 0], x_proj[:, 1], c=y, cmap='viridis', edgecolor='k', s=100)
    plt.title('PCA Projection of Iris Dataset')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(label='Species')
    plt.show()

if __name__ == "__main__":
    x, y = load_data()
    x_centered, mean = center_data(x)
    cov = compute_covariance(x_centered)
    eigvals, eigvecs = eigen_decompose(cov)
    x_proj = project(x_centered, eigvecs)
    plot_projection(x_proj, y)