import pprint

# Key Value pair
"""
Student

ID: 007
First Name: James
Last Name: Bond
Course: Spycraft
"""

word_definition = {
	"milieu": "the physical or social setting in which something occurs or develops",
	"light-year": "a unit of length in astronomy equal to the distance that light travels in one year in a vacuum or about 5.88 trillion miles (9.46 trillion kilometers)"
	}
# pprint.pprint(word_definition)

student = {
	"007": ["James", "Bond", "Spycraft"],
	}

# Let's say we have many students. We can represent them like this.
students = {
	"007": {"First Name":"James", "Last Name": "Bond", "Course": "Spycraft"},
	"008": {"First Name":"Marie", "Last Name": "Moreau", "Course": "Crime fighting"},
	}

pprint.pprint(student)
pprint.pprint(students)
