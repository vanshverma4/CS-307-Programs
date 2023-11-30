#program 7

A=lambda x:x+6
print(A(6))

list1=list(map(int,input().split()))
print(list1)

y=lambda x,z: z if A(z)+3>x else 6

print(y(6,3))

