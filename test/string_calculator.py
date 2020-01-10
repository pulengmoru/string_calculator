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
print(add("22"))