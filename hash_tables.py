book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
print(book["avocado"])

value = book.get("avocado")
print(value)
value = book.get("alksjdflsa")
print(value)