#-usr/bin/env python3


#comment for change for travis build
def calculate (myarg): 
	stack = list()
	for token in myarg.split(): 
		if token ==
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1+arg2
			stack.append(result)
		elif token ==
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1+arg2
			stack.append(result)
		else: 
			stack.append(int(token))
	print(stack)
	return stack.pop()
def main():
	while True:
		calculate(input("rpm calc> "))
if __name__ == '__main__':
	main()
