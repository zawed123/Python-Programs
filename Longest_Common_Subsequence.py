# https://www.facebook.com/fort.m.7/posts/385714229262556
# Subscribed by voice kaushik

#Longest Common Subsequence using Numpy
import numpy as np
#input both the string
st=input("Enter the string: ")
sub=input("Enter the sequence: ")
l1=[0]
l2=[0]
for i in st:
    l2.append(i)                                       #append all the characters of string to the list
for i in sub:
    l1.append(i)                                       #append all the characters of string to the list
r=len(sub)+1                                           #no of rows in the matrix
c=len(st)+1                                            #no of columns in the matrix
M=np.zeros((r,c))                                      #creating a matrix of r*c dimension having all elements as zeros
for i in range(1,r):
    for j in range(1,c):
        if l1[i]==l2[j]:                                #if both the char in the lists matches then add 1 to the diagonal element
            M[i,j]=1+M[i-1,j-1]
        else:
            M[i,j]=max(M[i,j-1],M[i-1,j])
print(f'The length of the longest subsequence is {M[-1,-1]}')  #print the length of longest subsequence
s=''                                            #a string to print the longest subsequence
while j>0 and i>0:                              #continue loop until j>0 and i>0
    if l1[i]==l2[j]:                            #if both the char in the list matches then then add the char to the string s
        s=s+l2[j]
        i=i-1
        j=j-1
    elif M[i,j-1]>M[i-1,j]:
        j=j-1
    else:
        i=i-1
print(f'The longest subsequence is "{s[::-1]}"')  #s[::-1] reverses the string s
