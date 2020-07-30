
# Time O(N) and Space is also O(N) due to the hashmap we need to maintain 

# def findPair(a,target):
# 	d ={}

# 	for i in range(len(a)):
# 		temp = target - a[i]
# 		if temp in d:
# 			return True

# 		d[a[i]] = i
# 	return False

# This is used if we want the indexes of all the pairs in the array with sum equal to the array
def findPair(a,s):
	d ={}
	res =[]
	for idx, val in enumerate(a):
		temp = s - val
		if temp in d:
			res.append((d[temp],idx))
		d[val] = idx
	return res

a =[3 ,2 ,8 ,15,-8 ,18,-1]

target = 17
res = findPair(a,target)
print(res)

