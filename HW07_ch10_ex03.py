# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#from itertools import accumulate


def cumulative_sum(lst):
	new_list = []
	running_sum = 0
	for item in lst:
		running_sum = item + running_sum
		new_list.append(running_sum)

	return new_list

def main():
	pass
#	result = cumulative_sum([1,2,3])
#	print(result)
#main()
