
# Time :- O(N) as we will iterate through the array once
# Space :- O(1) Constant space as it does not save the elements in set or hashtable
def duplicate(arr,n):

	# Iterate through the array
	for i in range(n):
		# arr[i] will give the element at and take its absolute value 
		# arr[value of arr[i] -1 ] -1 is done to make the index as 0 based 
		# if the value is positive then mark it as negative 
		if arr[abs(arr[i])-1] >=0 :
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
		#  If the value is already negative then print that element as it is the repeating element
		else:
			print(arr[i])



a = [1,3,4,2,1,2,5,6,7,8,3]
n =len(a)
duplicate(a,n)
