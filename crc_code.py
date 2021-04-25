import string
import sys
d={}
x=1
d[" "]=27


d2={}
d2[str(27)]=" "

alphabets = string.ascii_uppercase
for i in alphabets:
	d[str(i)]=x
	d2[str(x)]=str(i)
	x+=1


def convert_to_binary(st):
		binary_st=""
		for i in st:
			try:
				n=d[str(i)]
			except:
				sys.exit("Tried sending incorrect data")
			binary_st=binary_st + str(bin(n).replace("0b", "") )
		return binary_st

def xor(a, b): 
	result = "" 
	for i in range(1, len(b)): 
		if a[i] != b[i]: 
			result+="1"
		else: 
			result+="0" 
	return result 


def mod2div(divident, divisor): 
    div_len = len(divisor) 
    temp = divident[0 : div_len] 
   
    while div_len<len(divident): 
        if temp[0] == '1': 
            temp = xor(divisor, temp) + divident[div_len]    
        else: 
            temp = xor('0'*div_len, temp) + divident[div_len]    
        div_len += 1
   
    if temp[0] == '1': 
        temp = xor(divisor, temp) 
    else: 
        temp = xor('0'*div_len, temp) 
   
    checkword = temp 
    return checkword 


def binary_to_crc(binary_st):
	key="1011"
	appended_binary_st=binary_st+"000"

	remainder=mod2div(appended_binary_st,key) 
	return remainder

def text_to_cipher(st):
	if len(st)%3==1:
		st+="  "
	elif len(st)%3==2:
		st+=" "

	l=[]
	for i in st:
		l.append(d[str(i)])

	matrix=[]
	
	row = 3
	col = int(len(st)/3)
	matrix=[]
	for x in range (row): 
		matrix.append([])
		for y in range(0, col):
			matrix[x].append("&&")

	row=0
	col=0
	count=0
	#print(l)

	for i in l:
		#print(row)
		#print(col)
		matrix[row][col]=i
		row=(row+1)%3
		count+=1
		col = int(count/3)
		
	a=[[-3,-3,-4],[0,1,1],[4,3,4]]
	
	result=[]	
	for i in range(3):
		result.append([])
		for j in range(len(matrix[0])):
			result[i].append(0)
			for k in range(3):   
				result[i][j]+= a[i][k]*int(matrix[k][j])
	#print(matrix)
	#print(a)
	#print(result)
	return result




def cipher_to_text(b):
	a=[[1,0,1],[4,4,3],[-4,-3,-3]]

	result=[]
	row=3
	col=len(b[0])

	result=[]

	for i in range(3):
		result.append([])
		for j in range(len(b[0])):
			result[i].append(0)
			for k in range(3):   
				result[i][j]+= a[i][k]*int(b[k][j])
	
	st=""
	for j in range(len(result[0])):
		for i in range(3):
			aaa=str(result[i][j])
			st+=str(d2[aaa])
	return st

import json

def encyrpt_data(st):
	a=convert_to_binary(st.rstrip())
	encyrpted_data1= binary_to_crc(a)
	encyrpted_data2= str(text_to_cipher(st))
	final_msg = encyrpted_data1 + "**" + encyrpted_data2
	return final_msg

def decrypt_data(st):
	a,b=st.split("**")
	final_msg=cipher_to_text(eval(b))
	aa=convert_to_binary(final_msg.rstrip())
	remainder= binary_to_crc(aa)
	if str(remainder)!=str(a):
		final_msg="Recvd error"
	return final_msg