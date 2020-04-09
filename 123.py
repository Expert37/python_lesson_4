array = ["Bob", "Alex", "Bob", "John", "Jack", "Will", "Jacob", "Grace", "John", "David", "Bob"]

temp_dict = {i: array.count(i) for i in array}
a = list(temp_dict.items())
a.sort(key=lambda i: i[1], reverse=True)
for i in a[0:1]:
    print(i[0], ':', i[1])



