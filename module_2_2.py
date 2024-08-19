firs=input('введите3 числа')
second= input()
third=input()

if int(firs)==int(second)==int(third):
    print(3)
elif int(firs)==int(third) or int(firs)==int(second) or int(second)==int(third):
    print(2)
else:
    print(0)