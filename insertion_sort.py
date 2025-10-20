
a=[4,1,3,2]

for i in range (1,len(a)):
 temp=a[i]
 j=i-1
 while j>=0 and a[j]>temp:
    a[j+1]=a[j]
    j=j-1
 a[j+1]=temp
print(a)
