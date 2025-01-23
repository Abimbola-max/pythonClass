my_dict = {"name": "Abimbola", "age": 25, "city": "New York"} #name, age , city are key, while whatever they are carrying is the values

if "city" in my_dict: #in keyword is a powerful keyword to check if an element is present in a variable
		print('City is in my dictionary') 

del my_dict["city"]# to delete a key from the dictionary you can use the "del" key word or function to delete it 
print(my_dict)

my_dict["city"] = "America" #to change the value in a dictionary,it can be changed like this way, using the key and what you want to change it to

print(my_dict)


print(my_dict)
print(my_dict["name"]) # toprint only the name, use this method 
print(my_dict.get("salary", "Not Available")) #get can take two parameters and if you remove the second parameter when the first parameter is not available in the dictionary it will show "none"
print(my_dict.get("age")) #to get the age alone, use the get method 

for key in my_dict: #this method is used to get the keys of the dictionary, it could be any variable instead of key
	print(key)

for value in my_dict.values():#this method is used to get the values of the dictionary, it could be any variable instead of values
	print(value)

for key, value in my_dict.items(): #this method would get the keys and values 
	print(f"{key}: {value}")


squared = {x:x ** 2 for x in range(1,6)} 
print(squared)


keys = ["name","age","city"]
values = ["Alice", 25, "New York"]

my_dict = {"name": "Alice","age": 25}
new_data = {"city": "New York", "age": 26}

for key, value in new_data.items():
	my_dict[key] = value
print("my dict is" , my_dict)

nested_dict = {"person1" : {"name": "Alice", "age": 25}, "person2": {"name": "Bob", "age": 30}}

nested_dict["person1"]["city"] = "New York"

print("the nested dictionary is ",nested_dict)


new_data = {"city": "Los Angeles", "profession": "engineer"}

nested_dict["person2"].update(new_data)

print(nested_dict)



















