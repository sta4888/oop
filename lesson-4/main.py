class Person:
    age = 16
    name = 'Max'


print(getattr(Person, 'x', "Imposible"))
setattr(Person, 'x', 5 )
Person.k = 20
print(Person.k)
print(Person.__dict__)  # made in proxy - выводит словарь полей и методов
