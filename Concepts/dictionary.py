car = {
  "brand": "Ford", #brand is the key, ford is the value
  "model": "Mustang",
  "year": 1964
}

x = car.items() #gets pairs of key value
y = car.keys() #gets keys
z = car.values() #gets values
# these are only used to view the keys and values.
# To manipulate them or iterate over them, you need to list() them or [] them
a = list(car.items())
b = list(car.keys()) 
c = list(car.values())
# now abc will print lists
#don't forget car.items() will return something in format of a,b, so make sure its like a,b = list(car.items())
print(f"{x}\n{y}\n{z}")
print(f"{a}\n{b}\n{c}")

#to get keys by value you can:
 
dic ={"geeks": "A","for":"B","geeks":"C"} 
 
value = {i for i in dic if dic[i]=="B"} #problem with this method is that it prints {"x"} isntead of x
print("key by value:",value[0])

#or... 

# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}
 
# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
 
# print key with val 100
position = val_list.index(100)
print(key_list[position])

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# Sort by key
dict(sorted(people.items()))
#output {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

# Sort by value
dict(sorted(people.items(), key=lambda item: item[1]))
#output {2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}

for x in thisdict:
  print(x)
# x will be the keys of thisdict