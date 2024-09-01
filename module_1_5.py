immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
# Главное свойство кортежа - это невозможность изменить содержимое кортежа после его создания
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[0] = 1
mutable_list[1] = 2
print(mutable_list)
