# Define class MyFirstClass
class MyFirstClass:
    # Add a print statement inside it
    print("Who wrote this?")


# Create a string variable named index
index = "Author-Book"

# Define function hand_list()


def hand_list(self, philosopher, book):
    # Write a print statement using the print() function and pass the class variable by accessing it
    print(MyFirstClass.index)
    # Write a print statement that will give the desired output
    print(philosopher + " wrote the book: " + book)


# Create and instantiate an object of that class, called whodunnit
whodunnit = MyFirstClass()

# Call method hand_list() over this object "whodunnit" and pass two values to it
whodunnit.hand_list("Sun Tzu", "The Art of War")
