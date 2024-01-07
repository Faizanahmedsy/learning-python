# This is a list which is a ordered collection, elements of the list can be of any datatype
fruits = [4, True, "hi"]


# Append method is used to push an element in the array, the new element is added in the last
fruits.append("This was added in the last")



# Extend method is used to push an array in side another array, the new array is added after last element of first array 
fruits.extend([1,2,3,4])


print(fruits)


print("There are " + str(len(fruits)) + " Fruits")