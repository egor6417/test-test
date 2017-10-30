data=input().split()
A=list(map(int,data)
d=A[-1]
for i in range (0, len(A),-1)
	A[i]=A[i+1]
A[len(A)-1]=d

''' data=input().split(A=list(map(int,data))
for i in range(len(A)-1):
	if (A[i]>A[i-1])and (A[i]>A[i+1]):
		k=k+1
print (k)

data=input().split()
A=list(map(int,data))
for i in range(len(A)-1):
	if (A[i]>0 and A[i+1]>0)or (A[i]<0 and A[i+1]<0):
		print(A[i],A[i+1])
		break '''