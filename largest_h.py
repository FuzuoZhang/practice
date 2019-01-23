def largest_h(data):
	n = len(data)
	index = [0 for i in range(n+1)]
	for i in range(n):
		index[min(n,data[i])] += 1
	for i in range(n,-1,-1):
		if(i==n and index[i]>=n):
			return i
		if(i<n):
			index[i]+=index[i+1]
			if(index[i]>=i):
				return i
				
if __name__=="__main__":
	#data = [1,2,6,3,7,5,4]
	data = [5,5,5,5,5]
	print(largest_h(data))




