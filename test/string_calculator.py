import re

# Creating the add function
def add(num_string):
	num_string = r'{}'.format(num_string)
	extracted_numbers = re.findall(r"-?\d+", num_string)
	negatives = getAllNegatives(extracted_numbers)
	total_sum = 0

	# check if there are negative numbers and throw a relevant exception
	if len(negatives) > 0:
		error_msg = 'ERROR: negatives not allowed '
		for i in range(len(negatives)):
			if i != len(negatives)-1:
				error_msg += str(negatives[i]) + ','
			else:
				error_msg += str(negatives[i])
		raise Exception (error_msg)
	else:
		for num in extracted_numbers:
			if int(num) < 1000:
				total_sum += int(num)
	return total_sum
	
def getAllNegatives(nums):
	negs = []
	for num in nums:
		if int(num) < 0:
			negs.append(int(num))
	return negs	



total_sum  = add("-1")
print(total_sum)