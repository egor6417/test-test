data=input().split()
A=list(map(int,data)
p=-1
y=A[len(A)-1]
for i in range (0, len(A)-1,-1, p):
	A[i]=A[i+1]
A[0]=y
for i in range (0, len(A)):
	print(A[i], end='')