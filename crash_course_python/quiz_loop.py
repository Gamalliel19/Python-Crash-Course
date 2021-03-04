# 1
number = 1
while number <= 7:
	print(number, end=" ")
	number += 1

# 2
def show_letters(word):
	for char in word:
		print(char)

show_letters("Hello")
# Should print one line per letter

# 3
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n > 0):
		count += 1
		n = n//10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

# 4
def multiplication_table(start, stop):
	for x in range(start, stop + 1):
		for y in range(start, stop + 1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

# 5
def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x > stop:
            return_string += str(x)+","
            x -= 1
    else:
        return_string = "Counting up: "
        while x < stop:
            return_string += str(x)+","
            x += 1
    return_string += str(stop)
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# 6
def even_numbers(maximum):
    return_string = ""
    for x in range(0, maximum + 1):
        if x != 0 and x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# 7

# def decade_counter():
#     year = 20
#     while year < 50:
# 		year += 10
# 	return year

# 8
for x in range(1, 10, 3):
    print(x)

# 9
for x in range(10):
    for y in range(x):
        print(y)

# 10
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)
