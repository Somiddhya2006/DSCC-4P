import numpy as np 
A= np.array([[20,1,-2],[3,20,-1],[2,-3,20]])
B=np.array([17,-18,25])
x=np.zeros(3)
n=8
for i in range (n):
    x[0]=(B[0]-x[1]+2*x[2])/20
    x[1]=(B[1]-3*x[0]+x[2])/20
    x[2]=(B[2]-2*x[0]+3*x[1])/20
    print(f"Iteration:{i+1}, x,y,z:{x}")
    
print("Value of x,y,z using Gauss Seidel")
print(x)

print("Verificartion using numpy linalg")
x_1=np.linalg.solve(A,B)
print(x_1)