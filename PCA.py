'''
Study on PCA and its coefficients
'''

import numpy as np
from sklearn.decomposition import PCA

# Given X, return transformed X and pca object
def apply_PCA(X):
    pca = PCA()
    return pca.fit_transform(X), pca

# A linear model that returns y = Wx + b
def linear_model(X, W, b):
    return np.dot(X, W.T) + b.T

# Restate the coefficients in terms of the original variables,
# given the coefficients and pca object
def restate_coef(W, b, pca):
    W_new = np.dot(W, pca.components_)
    b_new = np.repeat([pca.mean_], b.shape[1], axis=0)
    b_new = b - np.dot(b_new, W_new.T).T
    return W_new, b_new

# Create a dummy data
X = np.random.rand(4,3)
print("\nDummy data X =")
print(X)

# Apply PCA on X
X_pca, pca = apply_PCA(X)
print("\nPCA transformed X =")
print(X_pca)

print("\n---------------------------------------")
print("Initialize coefficients for a linear model")
print("---------------------------------------")
W = np.random.randn(1, X.shape[1])
b = np.random.randn(1, X.shape[0])
print("W = ", W)
print("b = ", b)

print("\n---------------------------------------")
print("Apply the linear model on PCA transformed X")
print("---------------------------------------")
print("W(x_PCA) + b = ")
print(linear_model(X_pca, W, b))

print("\n---------------------------------------")
print("Restate coefficients in terms of original variables")
print("---------------------------------------")
W_re, b_re = restate_coef(W, b, pca)
print("Restated W = ", W_re)
print("Restated b = ", b_re)
print("\n---------------------------------------")
print("Apply the linear model on original X and restated coefficients")
print("---------------------------------------")
print("(restated_W)(original_x) + (restated_b) = ")
print(linear_model(X, W_re, b_re))