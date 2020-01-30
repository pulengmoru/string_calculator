import re

def add(num_string):
	num_string = r'{}'.format(num_string)
	
	
	if len(num_string) == 0:
		return 0

	if len(num_string) == 1:
		return int(num_string)

	if len(num_string)>=3 and "," not in num_string:
		return int(num_string)
	else:
		nums = num_string.split(",")
		total = 0
		for n in nums:
			total = total + int(n)
		return total 	

def getAllNegatives(nums):
	negs = []
	for num in nums:
		if int(num) < 0:
			negs.append(int(num))
	return negs	

reg = re.findall(r"-?\d+", num_string)
def add(reg):
	for number in reg:
		total = 0
		if int(number) < 1000:
			total = total + int(number)
	return total

 
 

# 	# exctract negative numbers from reg list

negs = getAllNegatives(reg)
if len(negs) > 0:
	error = 'ERROR: negatives not allowed '
	for i in range(len(negs)):
		if i == len(negs) - 1:
			error = error + negs[i]
		else:
			error = error + negs[i] + ','
		raise Exception(error)


total_sum  = add("1,2,3,-4")