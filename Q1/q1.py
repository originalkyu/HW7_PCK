import numpy as np
import pandas as pd
def main():
    # Q1_1
    arr = np.array([[1,2],[3,4]])
    eig_val, eig_vec = np.linalg.eig(arr)
    det = np.linalg.det(arr)
    print("Eigenvalue: {}".format(eig_val),end='\n\n')
    print("Eigenvector: {}".format(eig_vec),end='\n\n')
    print("Determinant: {}".format(det),end='\n\n')

    # Q1_2
    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])
    print("Cross product: {}".format(np.cross(vec1, vec2)), end="\n\n")

    # Q1_3
    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    sol = np.array([-15,-21,18])
    print("Solution: {}".format(np.linalg.solve(A,sol)))

if __name__ == "__main__":
    main()