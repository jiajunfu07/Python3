from sys import argv
script, first, second = argv

def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
	print(f"arg1: {arg1}")

def print_none():
	print("I got nothing.")

print_two(first, second)
print_two_again(second, first)
print_one(first)
print_none()
