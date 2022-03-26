"""sets can only store one element of the same value in them, all valus are unique.
We can use this to our advantage by being able discard non-unique values that are added to the data structure.
"""
#here's some example text we can use. by using the set we can receive all the unique words used within this text.  
text = "this text is meant to be an example for how we can use sets, there is multiple repeated words within this example and we can find each unique word inside the text by addding them all to a set."
#here is a list we can use to receive all the unique values from it. 
unique_value_list = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4]

#to start lets create a set, in python sets are created with the keyword set.
practice_set = set()

#now lets split this text into independent words by using the .split() function.
#this splits the text into a list seperating each word by a space.
word_list = text.split(" ")

#now we can add all the words in this list to the set.
print("original sentence: ", end="")
for word in word_list:
    #one of the convenient things abouts sets is that adding a value that is already in the set will not be added, as well adding an item has O(1) efficiency.
    practice_set.add(word)
    print(f"{word} ", end="")
print()

#now when we print every item in this set, you'll notice that the words are not in order. this is due to the sets hash system.
print("sets words: ", end="")
for item in practice_set:
    print(f"{item} ", end="")
print()

#we can also see the amount of item in the set compared to the normal word_list. the duplicates are not added.
print(f"set size: {len(practice_set)}, list size: {len(word_list)}, thats means there are {len(word_list) - len(practice_set)} unique words in the text!")

#lets look at one more example to show sets and there values. lets make a new set
number_set = set()

#now lets add all the numbers from the unique values list to the set.
for item in unique_value_list:
    number_set.add(item)

#now lets print out all the items in the set.
print("set with values 1,2,3,4: ", end="")
for item in number_set:
    print(f"{item} ", end="")
print()

#these numbers are in order, why is that but not the text? well every value in a set is organized into a hash value that we use to find the exact location of the
#value in the set, the number 1  has the hash value of 1, so it comes first. but the computer will generate a hash value for a word and that will cause
#different values to hold different places.
#a hash value for the word "text" can be seen below. the hash value may be different in your set, but this is an example fo a conversion.
hash_value = hash("text")
print(f"hash value for the word 'text': {hash_value}")




