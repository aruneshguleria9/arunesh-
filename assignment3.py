#ques_1.
a=[]
n=int(input("enter the size of list"))
for i in range(n):
    w=int(input())
    a.append(w)
print(a)
#ques_2.
b=["google","facebook","apple","tesla","microsoft"]
a.extend(b)
print(a)
#ques_3.
a=[1,2,2,2,2,4,5,5,3]
print(a.count(2))
#ques_4.
a=[14,12,334,67,4,34,6,7,2]
a.sort()
print(a)
#ques_5.
a=[2,6,7,4,5,3]
a2=[62,78,33,22,14]
a.sort()
a2.sort()
a.extend(a2)
print("the merged array:",a)
a.sort()
print("the merged sorted array:",a)
#ques_6.
even=0
odd=0
for i in a:
	if(i%2==0):
	 even=even+1
	else:
	 odd=odd+1
print("count of even numbers:",even)
print("count of odd numbers:",odd)
#ques_7
#TUPLES not done
#STRINGS
#ques_1.
a=input("enter the string\n")
print(a.upper())
#ques_2.
a=input("enter a string\n")
count=0;
for i in range(len(a)):
    if a.isdigit():
       count=1;
    else:
        count=0;
        break;
if count==1:
    print("True")
else:
    print("False")
#ques_3.
a="Hello World"
print(a.replace("World","Rawat"))
