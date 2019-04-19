
'''
def quicksort(data,low,hig):
	#sort the part of [data[low],data[hig]), increasing
	if(hig-low<=1):
		return

	sta = data[low]
	lindex = low+1
	rindex = hig-1
	mindex = low

	while(lindex<=rindex):
		if(data[lindex]<=sta):
			data[mindex] = data[lindex]
			mindex += 1
			lindex += 1
		elif(data[rindex]>=sta):
			rindex -= 1
		elif(data[rindex]<sta and data[lindex]>sta):
			data[mindex] = data[rindex]
			data[rindex] = data[lindex]
			mindex += 1
			lindex += 1
			rindex -= 1
	data[mindex] = sta

	quicksort(data,0,mindex)
	quicksort(data,mindex+1,hig)
	return 
'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__=="__main__":
	data = [1,8,4,2,4,2,0,3,7,11,0]
	data = [0,0,0,1]
	print("data:", data)
	data_sort = quicksort(data)
	print("sorted data:", data_sort)



