def repeat(x):
	r=[]
	for i in range(n-1):
		for j in range(i+1,n):
			if x[j]==x[i]:
				r.append(j)
	return x[min(r)]			
n=int(input())
l=list(map(int,input().split()))
k=repeat(l)
print(k)
