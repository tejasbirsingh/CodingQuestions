def primeNumbers(primeList,n):
	p=2
	while(p*p <= n):
		if primeList[p] == True:
			for i in range(p*p,n+1,p):
				primeList[i] = False
		p+=1


n =100

primeList =[True for i in range(n+1)]
primeList[0]=primeList[1]=False

primeNumbers(primeList,n)

for i in range(n):
	if primeList[i]==True:
		print(i,end=' ')

print(primeList[19])