grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik','Aaron'}
a=sum(grades[0])/len(grades[0])
b=sum(grades[1])/len(grades[1])
j=sum(grades[2])/len(grades[2])
s=sum(grades[3])/len(grades[3])
k=sum(grades[4])/len(grades[4])
st=sorted(students)
students_={st[0]:a,st[1]:b,st[2]:j,st[3]:s,st[4]:k}
print(students_)
