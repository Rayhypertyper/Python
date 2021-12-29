food_list = ["pizza", "poutine", "fries"]
# print(food_list)
# print(food_list[1])
# print(food_list[-1])
# print(food_list[0:2])

# print(len(food_list))

# if "pizza" in food_list:
#     print("Yes, 'apple' is in the fruit list")
#     other_list = ["apple", "banana", "cherry", 1, 10, "a", 5.3]

# #adding to end of food list
# food_list.append("orange")
# print(food_list)

# food_list.insert(1,"pear")
# print(food_list)

# food_list.remove("pizza")
# print(food_list)

# food_list.pop(1)#removing
# food_list.pop()
# food_list.clear()#clear

# for i in range(len(food_list)):
#     print(food_list[1]) 

# for food in food_list:
#     print(food) #printing all things from list

# new_food_list = food_list

# new_fruit_list = food_list.copy #makes new list duplciate

# list1 = [6,1,19,21,3]
# list1.sort()#sorts the list from smol to big
# print(list1) 
# list1.sort(reverse=True) #
# new_list = sorted(list1)
# print(list)

#making new list sorted
# new_list = sorted(list1)
# print(new_list)
# print(list1)

list1 = ["a", "b", "c"]
list2 = [1,2,3]
# list3 = list1 + list2
# print (list3) #prints both lists 

# list1.append(list2)
# print(list1) #adds list 2 into list1
# list1.extend(list2)
# print(list1) #prints first + second list basically more simple den prev method

# fruit_tuple = ("apple", "banana", "cherry")
# print(fruit_tuple)
# print(fruit_tuple[1]) #index 1
# print(fruit_tuple[-1]) #last thing on list
# print(fruit_tuple[1:2]) #prints items from 1 to 2 not including 2

# for fruit in fruit_tuple:
#     print(fruit) #prints the list with no brackets or ''

# if "apple" in fruit_tuple:
#     print("Yes, 'apple is in the fruit tuple")

fruit_set = {"apple", "cherry", "banana"}
fruit_set.add("orange") #will add orange to set in random order
fruit_set.add("apple") #wont add same thing again to set
print(fruit_set)


print(sorted(fruit_set)) #sorts it by alphabetically order