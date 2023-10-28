# Program to print 3 coordinates i,j,k on 3D grid# when 3 integers are given representing the  dimensions of cuboid
# Another integer n is also given
# Sum of i +j+k not equal to n
# 0<=i<=x;0<=j<=y;0<=<=k<=z

x= int(input("Enter the value"))
y= int(input("Enter the value"))
z= int(input("Enter the value"))
n= int(input("Enter the value"))
coords=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)
if i+j+k !=n]
print(coords)