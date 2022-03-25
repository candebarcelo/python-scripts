from functools import reduce
from typing import List


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sasha(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat

# 2 Create a list of all of the pets (create 3 cat instances from the above)


my_cats = [Simon('simon', 1), Sally('sally', 4), Sasha('sasha', 10)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance

my_pets.walk()


class SuperList(List):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, List))


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.capitalize()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()
print(list(zip(my_numbers, my_strings)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def passed(item):
    return item >= 50


print(list(filter(passed, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

my_numbers.extend(scores)
print(list(my_numbers))


def sumLists(acc, item):
    return acc + item


print(reduce(sumLists, my_numbers, 0))


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({char for char in some_list if some_list.count(char) > 1})

print(duplicates)


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrappy(*args, **kwargs):
        if args[0]['valid'] == True:
            fn(*args, **kwargs)
    return wrappy


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)


def fib(number):
    listita = [0]
    for item in range(0, number, 1):
        if item == 0:
            listita.append(1)
        else:
            listita.append(int(listita[item-1]) + int(listita[item]))

    return listita


print(fib(20))
