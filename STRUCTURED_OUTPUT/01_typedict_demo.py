from typing import TypedDict

class Person(TypedDict):
    first_name: str
    last_name: str
    age: int

person001= Person(
    first_name='John',
    last_name='Doe',
    age=22
)

person002 : Person = {'first_name': 'Gunjan',
                          'last_name': 'Kumar',
                          'age': 32
                          }

print("==person001==")
print(person001)
print("==person002==")
print(person002)