# Python3 code to demonstrate working of
# Maximum in Rows Range
# Using max() + slicing

# initializing list
test_list = [[4, 3, 6], [9, 1, 3], [4, 5, 2],
			[9, 10, 3], [5, 9, 12], [3, 14, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 4

res = 0
for idx in range(i, j):

	# getting max in range
	res = max(max(test_list[idx]), res)

# printing result
print("The maximum element in row range ? : " + str(res))
