product = {
    "name":"book",
    "quantity":3,
    "price":4.99
}

person = {
    "first_name": "ryan",
    "last_name": "ray"
}

print(person.items())
person.clear()

print(person)

products = [
    {"name": 'book', "price": 10.00},
    {"name": 'laptop', "price": 1000}
]
print(products)


print(person.items())
del person
print(person)


print(person)
products = [
    {"name": 'book', "price":10.99}
]

print(products)