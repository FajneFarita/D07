# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
import copy


def is_sorted(lst):
	old_list = copy.copy(lst)
	lst.sort()
	if old_list == lst:
		return True
	else:
		return False	

def main():
#	is_sorted(['a', 'b', 'c'])
#	is_sorted(["b", "c", "a"])
#main()