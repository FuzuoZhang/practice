def weather(A):
	n = len(A)
	B = A.copy()
	C = [i for i in range(n)]
	D = [-1 for i in range(n)]
	for i in range(n-1,-1,-1):
		k = i+1
		tmp = len(B)
		for j in range(i+1,tmp):
			if(B[k]>B[i]):
				D[i] = C[k]
				break
			else:
				del B[k]
				del C[k]
	return D

def fun(x,a):
	return x*x-a

def df(x):
	return 2*x

def mysqrt(a,eps):
	x = a
	while(1):
		x = x - fun(x,a)/df(x)
		if(abs(fun(x,a))<eps):
			break
	return x

def testWeather():
	#A = [0 for i in range(6)]
	#for i in range(6):
	#	A[i] = int(input())
	A = [23,22,15,14,17,23]
	B = weather(A)
	for i in range(6):
		print(B[i])

def testSqrt():
	print(mysqrt(2,0.00001))
if __name__=="__main__":
	testWeather()
	testSqrt()
	
