import numpy as np
from scipy import sparse

x= np.array([[1,2,3],[4,5,6]])
print("x:\n{}".format(x))

#ctreating a 2D Numpy array with a diagonal of ones and zeros everywhere else
eye = np.eye(4)
print("eye:\n{}".format(eye))

# Convert the NumPy array to a SciPy sparse matrix in CSR format
# Only the nonzero entries are stored
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))


#printing the same data using the COO format method


"""data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n{}".format(eye_coo))"""








