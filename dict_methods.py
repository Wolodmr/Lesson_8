student = {}
student['name'] = 'John Doe'
student['age'] = 26
student['major'] = 'Computer Science'
print(student)
student['major'] = 'Electrical Engineering'
student['year'] = 'Senior'
print(student)
print(student.keys())
print(student.values())

list = [
{'title': 'Stories', 'author': 'Jack London', 'year': 2019},
{'title': 'Martin Eden', 'author': 'Jack London', 'year': 2021},
{'title': 'Ethics', 'author': 'Aristotel', 'year': 2020}
]
print(list[1]['title'])
print(list[2]['year'])
print(sorted(list, key = lambda item: item['year']))

courses = {'math':['John', 'Betty', 'Thom', 'Lucy', 'Jim'], 'history': ['Barby', 'Joe', 'Melony'], 'chemistry': ['Ann', 'Mary', 'Bobby', 'Stan']}
l = ['Mary', 'Bill', 'Colton', 'Gretha', 'Sally']

courses['math'].extend(l)
print(courses)
del courses['history'][2]
print(courses)
print(courses['chemistry'])
courses['physics'] = ['Roger', 'Nils', 'Astrid', 'Pelle']
print(courses)

for i in range(1, 10):
    if(i%5==0):    
        print(i)
else:
    print(f"{i} this is not printed because for loop is terminated because of break but not due to fail in condition")


c = sorted(courses['history'], key =lambda item: item[0])
c.sort(reverse = True)
print(c)

ls = dict(sorted(courses.items(), key = lambda item: item[0]))
print(ls)
