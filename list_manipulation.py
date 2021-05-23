def xor_lists(a,b):
	return (set(a)^set(b))

def and_lists(a, b):
	return (set(a) & set(b))

def left_lists(a, b):
	return (set(a) - set(b))

a = [1, 2, 3]
b = [2, 4, 6]
print(xor_lists(a, b))
print(and_lists(a, b))
print(left_lists(a, b))