def distinct_integers(input_list):
	if len(input_list)<=1:
		return 1

	distinct_values = set()
	index = 0

	while input_list[index] not in distinct_values:

		distinct_values.add(input_list[index])
		index = input_list[index]

	return len(distinct_values)


def distinct_integers_modified(input_list):
	first_repeat_location = len(input_list)

	for i in range(len(input_list)-1):
		element = input_list[i]

		if i==first_repeat_location:
			return first_repeat_location
		for j in range(i+1, len(input_list)):
			if element == input_list[j] and j<first_repeat_location:
				first_repeat_location = j
				break
	return first_repeat_location


