import re
def add(num_string):
	if len(num_string) == 0:
		return 0
	if len(num_string) == 1:
		return int(num_string)
	if len(num_string)>=2 and "," not in num_string:
		return int(num_string)
	else:
		nums = num_string.split(",")
		total = 0
		for n in nums:
			total = total + int(n)
		return total 

	if len(num_string)>2 and "," not in num_string:
		return int(num_string)
	else:
		nums = num_string.split(",")
		return sum(int(nums))
print(add("2,2"))

def add(s):
	if len(s) == 0:
		return 0
	reg = re.findall(r'\d+|-\d+' , s)
	total = 0

	# exctract negative numbers from reg list

	negs = getAllNegatives(reg)
	if len(negs) > 0:
		error = 'ERROR: negatives not allowed '
		for i in range(len(negs)):
			if i == len(negs) - 1:
				error = error + negs[i]
			else:
				error = error + negs[i] + ','
		raise Exception(error)

	for number in reg:
		if int(number) < 1000:
			total = total + int(number)
	return total
def getAllNegatives(nums):
	negs = []
	for num in nums:
		if int(num) < 0:
			negs.append(num)
	return negs 
total_sum  = add("//;\n1000,1;2")
print(total_sum)