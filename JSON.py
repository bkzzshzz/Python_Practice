import json
# some JSON:
x =  '''{"name" :"John", "age":30, "city":"New York"}'''
print(type(x))
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(type(y))


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))