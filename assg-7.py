#ques_1.
age=int(input("enter age to find "))
l={'ashu':20,'aru':21,'bidu':19,'papu':22}
for k,j in l.items():
    if j==age:
     print(k)
#ques_2.
students = {'ash': {'english': 20, 'maths': 40, 'science': 60},
          'jeet': {'english': 30, 'maths': 50, 'science': 70},
         'ashu': {'english': 89, 'maths': 78, 'science': 88},
         'dawat': {'english': 45, 'maths': 55, 'science': 75}}
name=input('enter name \n')
for n,s in students.items():
        if name==n:
            print("\nName",n)
            for marks in s:
                print(marks+':',s[marks])

