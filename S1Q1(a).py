import numpy as np
A=np.array([[4,-1,2],[3,6,-4],[2,-3,5]], dtype=float)
B=np.array([3,2,-2], dtype=float)
x=np.zeros(3)
n=10
for k in range (n):
    x[0]=(B[0]+x[1]-2*x[2])/4
    x[1]=(B[1]-3*x[0]+4*x[2])/6
    x[2]=(B[2]-2*x[0]+3*x[1])/5
    print(f"Iteration {k+1}: {x}")

print("Approximate solution using Gauss Seidel method")
print(x)

print("Verify using numpy linalg:")
x_1=np.linalg.solve(A,B)
print(x_1)