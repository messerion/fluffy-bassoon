immutable_var=(1,2,3,'a',True)
print(immutable_var)
#immutable_var[0]=200 #кортеж содержит неизменяемую коллекцию
mutable_list=['желтый','красный','синий',1,3,True]
mutable_list[1]='оранжевый'
print(mutable_list)
mutable_list.append(1.5)
print(mutable_list)