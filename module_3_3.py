def print_params(a = 1, b = 'строка', c = True):
    print(a , b , c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [8, False, 'привет']
values_dict ={'a': 25, 'b':'как дела?', 'c':True}
print_params(*values_list)
print_params(**values_dict)


values_list_ = [25.52, 'Строка']
print_params(*values_list_, 42)

