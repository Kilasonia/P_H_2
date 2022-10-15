# Реализуйте алгоритм перемешивания списка.


import random
list1 = [random.randint(0, 10) for i in range(random.randint(5, 20))]
print(f'source list :\n {list1}')
random.shuffle(list1)
print(f'list after mixing :\n{list1}')
