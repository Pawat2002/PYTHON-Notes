# to create a list used []
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim"]
        #     0        1        2
# printing lists / specific element in a list
print(friends)
print(friends[2])
# karen / Jim
print(friends[1:])

friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
# karen/Jim, stop at Oscar
print(friends[1:3])

# List extend functions, for adding list onto another list
friends.extend(lucky_numbers)
print(friends)

# append function, for adding element to the end of the list
friends.append("Creed")
print(friends)

# insert functions, for adding element into a specific index
friends.insert(1, "Kelly")

# remove function
friends.remove("Jim")
print(friends)

# pop function, by popping an item off of the list, basically remove last element of the list
friends.pop()
print(friends)

# index function, for looking for the position of an element in a list
print(friends.index("Kevin"))

# count function, count me how many times the element are in the list
print(friends.count("Jim"))

# sort function, sorting an element in order either alphabetically or numerically
lucky_numbers.sort()
print(lucky_numbers)

# reverse function, reverse the order of the list
lucky_numbers.reverse()
print(lucky_numbers)

# copy function, duplicating a list
friends2 = friends.copy()
print(friends2)

# clear functions, for clearing all element in a list
friends.clear()
print(friends)