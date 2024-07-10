my_dict = {'Misha': 1987, 'Sveta': 1993}
print(my_dict)
print(my_dict.get ('Misha'))
print(my_dict.get ('Ivan'))
my_dict.update({'Alex' : 1999,
             'Kamila' : 2002})
my_dict.pop('Sveta')
print(my_dict)
set_ = {1, 2, 4, 7, 1, 4, 7}
print(set_)
set_ = {1, 2, 4, 7, 1, 4, 7, 'Ананс', (2.15)}
print(set_)
list_ = [1, 2, 4, 7, 1, 4, 7,]
list_ = set(list_)
print(list_)
print(list_.discard(4))
print(list_)

