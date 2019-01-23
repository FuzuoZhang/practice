
def lowfilter(data, i, n):
	while(i<n):
		lindex = i*2+1
		rindex = i*2+2
		if (rindex < n):
			if(data[rindex]>data[i] and data[rindex]>=data[lindex]):
				data[i],data[rindex] = data[rindex],data[i]
				i = rindex
			elif(data[lindex]>data[i] and data[lindex]>=data[rindex]):
				data[i],data[lindex] = data[lindex],data[i]
				i = lindex
			else:
				i = n

		elif(lindex<n):
			if(data[lindex]>data[i]):
				data[lindex],data[i] = data[i],data[lindex]
				i = lindex
			else:
				i = n
		else:
			i = n
	return data

def crestack(data):
 	n= len(data)
 	for i in range((n>>1)-1, -1, -1):
 		data = lowfilter(data, i, n)
 	return data

def stacksort(data):
 	n = len(data)
 	data = crestack(data)
 	for i in range(n):
 		data[n-i-1],data[0] = data[0],data[n-i-1]
 		data = lowfilter(data,0,n-i-1)
 	return data

if __name__=="__main__":
	data = [6,4,1,7,0,-1]
	sortdata = stacksort(data.copy())
	print(data)
	print(sortdata)

