array = ["Bob", "Alex", "Bob", "John", "Jack", "Will", "Jacob", "Grace", "John", "David", "Bob"]
print(max(set(array), key=lambda x: array.count(x)))