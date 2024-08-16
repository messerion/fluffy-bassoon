my_dict={'Ирина':1992,'Алексей':1993,'Алиса':2022}
print(my_dict)
print(my_dict['Алексей'])
print(my_dict.get('Сергей','нет значения'))
my_dict.update({'Раиса':1955,'Владимир':1956})
a=my_dict.pop('Ирина')
print(a)
print(my_dict)
my_set={1,2,1,2,3,2,1,5,'apple','peach'}
print(my_set)
my_set.add('red')
my_set.add(7)
my_set.remove(5)
print(my_set)