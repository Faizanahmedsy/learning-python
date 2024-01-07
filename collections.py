# This is a list which is a ordered collection, elements of the list can be of any datatype
fruits = [4, True, "hi"]


# list are mutable if you change it from somewhere else the original list is going to be changed
newArrayThatWillChangeTheOriginalArray = fruits
newArrayThatWillChangeTheOriginalArray[0] = "first"


# You can make the copy of the original array by using [:] this operatior
copyOfTheOriginalArrThatWillNotChangeTheOriginalArray = fruits[:]
copyOfTheOriginalArrThatWillNotChangeTheOriginalArray[0] = "You cant see me"

# Append method is used to push an element in the list, the new element is added in the last
fruits.append("This was added in the last")



# Extend method is used to push an list in side another list, the new list is added after last element of first list 
# //It loops of all this elemets and just appends them in to the original list 
fruits.extend([1,2,3,"This will be removed because of pop method"])



# This removes the last elemet of the list
fruits.pop()




# pop method can also take index as an argument, it will remove the elemet in that perticular index

fruits.pop(3)


print(fruits)


print("There are " + str(len(fruits)) + " Fruits")