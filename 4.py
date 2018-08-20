#ques_1.
a=[4,5,7,8,9]
a.reverse()
print(a)
#ques_2.
b=input()
z=''
for i in range(0,len(b)):
    if b[i].isupper()==True:
        z=z+b[i]
print(z)
#ques_3.
a=[]
a=input()
b=[]
for i in a:
    b.append(int(i))
print(b)
#ques_4.
a=input()
c=a.split(",")
b=a[::-1]
print(a)
print(b)
if(a==b):
    print("palindrome")
else:
     print("not palindrome")
#ques_5.
import copy as c
l=[1,2,[4,5],6]
l1=c.deepcopy(l)
l[2][1]=8
print(l)
print(l1)
#shallow copy means constructing a new collection object and then populating it with refrences to the child objects found in the original
#deep copy makes the copying process recursive.it means first constructing a new collection object and then recursively populating it with copies of child objects found in original