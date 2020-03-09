import copy


#list x에 단어 넣기

#비교


def left(words,W,dp):
		
		n=len(words)
		
		
		for i in range (1,n):
			x=copy.deepcopy(words)
			y=copy.deepcopy(words)
			b=''
			a=False
			#c=False
			m=False
			#n=False
			if(i==n-2):
				if(W>=len(x[i])+len(x[i-1])+1):
					b=x[i-1]+' '+x[i]
					x[i]=''
					x[i-1]=b
					c=cal(x,W)
					dp.append(c)
					del x[i]
					#print("1")
					#print(x)
				m=True
				
				
				
			
			
			x=copy.deepcopy(words)
			y=copy.deepcopy(words)

			if(W>=len(x[i])+len(x[i-1])+1):
				b=x[i-1]+' '+x[i]
				x[i]=''
				x[i-1]=b
				c=cal(x,W)
				dp.append(c)
				del x[i]
				#print("1")
				#print(x)
				a=True
				#return left(x,W,dp)
				#print("1")
				#print(x)
		for i in range (0,n-1):		
			c=False
			n=False
			if(i==n-2):
				if(W>=len(x[i])+len(x[i+1])+1):
					b=x[i]+' '+x[i+1]
					x[i+1]=''
					x[i]=b
					c=cal(x,W)
					dp.append(c)
					del x[i+1]
					#print("1")
					#print(x)
				n=True
			if(W>=len(y[i])+len(y[i+1])+1):
				b=y[i]+' '+y[i+1]
				y[i]=''
				y[i+1]=b
				c=cal(y,W)
				dp.append(c)
				del y[i]
				#print("2")
				#print(y)
				c=True
				#return left(y,W,dp)
			
			if(m):
				if(n): return 
		
			
			if(a):
				if(c): return left(x,W,dp),left(y,W,dp)
				else: return left(x,W,dp)
			elif(c):return left(y,W,dp)
			

			

def cal(words,W):
		n=len(words)
		s=0
		for i in range(n):
			a=len(words[i])
			if(a!=0):
				b=(W-a)**3
				s=s+b
		return s
	
W = int(input())
words = input().split()
dp=[]

left(words,W,dp)


dp.sort(reverse=True)
k=len(dp)
#print(dp)
print(dp[k-1])
