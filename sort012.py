def sort012(a,  n):
	# d = {}
	# for i in range(n):
	# 	if a[i] in d:
	# 		d[a[i]] +=1
	# 	else:
	# 		d[a[i]] = 1

	# i = 0
	# for key , value in d.items():
	# 	for j in range(value):
	# 		a[i] = key
	# 		i+=1
	# return a

	l= 0
	m=0
	h=n-1
	while(m<=h):
		if a[m]==0:
			a[m],a[l] = a[l],a[m]
			l+=1
			m+=1

		elif a[m] ==1:
			m+=1
		else:
			a[m] ,a[h]= a[h] ,a[m]
			h-=1
	print(a)



a = [0,1,2,0,1,2]
print(sort012(a,len(a)))