# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def capitalize_nested(list):
	new_list = []
	for element in list:
		if isinstance(element, str):   #check if the element is string
			from_capital = element.capitalize()
			new_list.append(from_capital)
		else:	#if not a string, go inside and call the function again
			new_list.append(capitalize_nested(element))
	return new_list	




def main():
	pass
#	result = capitalize_nested(['apple', ['bear'], 'cat', [['dog']]])
#	print(result)
#main()

