#DarkSouL

# Python program to check if a given string is vowel Palindrome 

def vowel(c):
	v = list("aeiou")
	if c in v: 
	    return True
	return False
	
def palindrome(s): 
	v = []
	for i in s:
		if vowel(i):
		    v.append(i)
	if len(v)== 0: 
	    print("-1")
	else:
		x = v[::-1]
		f = 1
		for i in range(len(x)):
			if x[i]!= v[i]:
				f = 0
				break
		if f == 1: 
		    print("YES")
		else: 
		    print("NO")
		
s = 'abcuhuvmnba'
s1 = 'ExpectoPatronum'
print("Does ", s, "follows vowel palindrome ? -> ", end=" ")
palindrome(s.strip())
print("Does ", s1, "follows vowel palindrome ? -> ", end=" ")
palindrome(s1.strip())

