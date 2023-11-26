import pprint
# pprint is used to print things in a pretty manner.
# Literally stands for "pretty print"

# a dictionary where the key is a word, and the value is the definition of
# that word.
# Note: There are two key-value pairs seperated by a comma here.
word_definition = {
	"milieu": "the physical or social setting in which something occurs or develops",
	"light-year": "a unit of length in astronomy equal to the distance that light travels in one year in a vacuum or about 5.88 trillion miles (9.46 trillion kilometers)"
	}
# pprint.pprint(word_definition)

# A student that we will represent as a dictionary.
"""
Student

ID: 007
First Name: James
Last Name: Bond
Course: Spycraft
"""

# Here's a possible, valid representation of this student
student = {
	"007": ["James", "Bond", "Spycraft"],
	}

# A better representation is one that takes the guess work away, and is more
# explicit about that "James", "Bond", and "Spycraft" are.
# We can use the fact that the value of a dictionary can be anything, even another
# dictionary with its own key-value pairs.
student = {
	"007": {"First Name":"James", "Last Name": "Bond", "Course": "Spycraft"}
}
pprint.pprint(student)

# Let's say we have two students. We can represent them like this.
students = {
	"007": {"First Name":"James", "Last Name": "Bond", "Course": "Spycraft"},
	"008": {"First Name":"Marie", "Last Name": "Moreau", "Course": "Crime fighting"},
}

# pretty printing
pprint.pprint(student)
pprint.pprint(students)
