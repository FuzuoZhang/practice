def bubblesort(data,low,hig):
	low = max(0,low)
	hig = min(hig, len(data))
	n = hig - low
	for i in range(hig -1,low, -1):
		mark = 0
		for j in range(0,i):
			if(data[j]>data[j+1]):
				data[j],data[j+1] = data[j+1],data[j]
				mark = 1
		if(mark == 0):
			return

if __name__=="__main__":
	data = [1,8,4,2,4,2,0,3,7,11,0]
	print(data)
	bubblesort(data,0,len(data))
	print(data)


