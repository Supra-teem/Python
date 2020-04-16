#this program helps to find the Nth Ugly Number using Dynamic Prog
global m2,m3,m5,i2,i3,i5
i2=i3=i5=0
n=int(input("n= "))
ugly=[]
print(ugly)
ugly.append(1)
m2=ugly[i2]*2
m3=ugly[i3]*3
m5=ugly[i5]*5
def ugly_nums(n):
	global m2,m3,m5,i2,i3,i5
	for i in range(1,n):
		next_num=min(m2,m3,m5)
		print(ugly,"\n")
		ugly.insert(i,next_num)
		if(next_num==m2):
			i2+=1
			m2=ugly[i2]*2
		if(next_num==m3):
			i3+=1
			m3=ugly[i3]*3
		if(next_num==m5):
			i5+=1
			m5=ugly[i5]*5
	print(ugly)
	return next_num
print(ugly_nums(n))
