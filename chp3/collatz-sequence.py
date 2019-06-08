
def collatz(number):
	result = None
	if ((number % 2) == 0):
		result = number // 2
	else:
		result = (3 * number) + 1
	print(result)
	return (result)

while True:
	print("Enter a number:")
	input_str = input()
	try:
		input_int = int(input_str)
		break
	except ValueError:
		print("Please enter an interger!")

while True:
	ret = collatz(input_int)
	if (ret == 1):
		break
	input_int = ret
