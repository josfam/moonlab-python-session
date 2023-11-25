# CONDITIONALS, a.k.a how to ask questions

num1 = 5
num2 = 5
num3 = 8

# num1 less than num2
# if so "num1 is less than num2"

# if num1 < num2:
# 	print("num1 is less than num2")

# revised version
# if num1 < num2:
# 	print("num1 is less than num2")
# else:
# 	print("num1 is not less than num2")


# revised version with three scenarios
# if num1 < num2:
# 	print("num1 is less than num2")
# elif (num1 == num2):
# 	print("num1 is equal to num2")
# else:
# 	print("num1 is greater than num2")



# Another example of using elif

# Let's say we want to give a medal to a student whose name is Marie,
# however, we are going to be fed many names.
# Write a conditional ...

# Hawa - "Here is your Gold medal"
# Marie - "Here is your Silver medal"
# Aba - Bronze
# "Thanks for trying"

# student_name = "Lisa"

# if student_name == "Hawa":
# 	print("Here is your Gold medal")
# elif (student_name == "Marie"):
# 	print("Here is your Silver medal")
# elif (student_name == "Aba"):
# 	print("Here is your Bronze medal")
# else:
# 	print("Thanks for trying")


"""
If it is raining, and it is also Tuesday then Wear my yellow jacket

If the sun is out, but it is not hot, Don't wear a sweater
"""
# and, or, not

raining = True
tuesday = True
sun_is_out = True
day_is_hot = False

if (raining and tuesday):
	print("Wear my yellow jacket")

if (sun_is_out == True and day_is_hot == False):
	print("Don't wear a sweater")
