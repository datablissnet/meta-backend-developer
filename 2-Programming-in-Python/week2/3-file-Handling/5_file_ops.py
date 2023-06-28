# Define class MyFirstClass
class MyFirstClass:
    index = "Author-Book"
    # Add a print statement inside it
    print("Who wrote this?")

    def hand_list(self, philosopher, book, year):
        # Write a print statement using the print() function and pass the class variable by accessing it
        print(MyFirstClass.index)
        # Write a print statement that will give the desired output
        print(philosopher + " wrote the book: " + book + " in " + str(year))


# Create and instantiate an object of that class, called whodunnit
whodunnit = MyFirstClass()

# Call method hand_list() over this object "whodunnit" and pass two values to it
whodunnit.hand_list("Sun Tzu", "The Art of War", 1955)
