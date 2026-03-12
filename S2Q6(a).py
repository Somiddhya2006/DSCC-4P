import numpy as np 
A= np.array([[3,2,-1],[2,-3,4],[1,4,3]],dtype=float)
B= np.array([5,-3,7], dtype=float)
n=len(B)

Aug=np.hstack((A,B.reshape(-1,1)))

for i in range (n):
    max_row=np.argmax(abs(Aug[i:,i]))+i
    Aug[[i,max_row]]=Aug[[max_row,i]]
    
    for j in range(i+1,n):
        f=Aug[j,i]/Aug[i,i]
        Aug[j,i:]=Aug[j,i:]-f*Aug[i,i:]
    
x=np.zeros(n)
for i in range(n-1,-1,-1):
    x[i]=(Aug[i,-1]-np.dot(Aug[i,i+1:n], x[i+1:n]))/ Aug[i,i]
    
print("Solution using Gauss Elimination:",x)

print("Verification using linalg module:")
x_1=np.linalg.solve(A,B)
print(x_1)