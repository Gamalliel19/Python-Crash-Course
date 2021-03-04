# DEFINITION, WHILE LOOP, FOR LOOP, AND RECURSIVE
# def sum(x, y):
# 		return(x+y)
# print(sum(sum(1,2), sum(3,4)))

# print(((10 >= 5*2) and (10 <= 5*2)))

# x = 0

# while x < 5:
#     print("Not yet : " + str(x))
#     x += 1

# def attemps(n):
#     x = 1
#     while x < n:
#         print("Attempt : " + str(x))
#         x = x + 1
#     print("Done")

# attemps(10)

# def count_down(start_number):
#     current = start_number
#     while current > 0:
#         print(current)
#         current -= 1
#     print('Done')

# count_down(10)

# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	n = start
# 	while n < end:
#         print(n)
# 	    n += 1
# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# def print_range(start, end):
#     n = start
#     while n < end:
#         print(n)
#         n += 1
#     print(n)
# print_range(1, 5)

# nested loops
# teams = ["persija", "persib", "bali united", "barito putra"]
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(home_team + " vs " + away_team)

# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + " | " + str(right) + "]", end=" ")
#     print()

# for star_left in range(10):
#     for star_right in range(star_left, 10):
#         print("*", end=" ")
#     print()

# def factorial(n):
#     result = 1
#     for x in range(result, n):
#         result = result * x
#     return result

# for n in range(1, 10):
#     print(n, factorial(n-1))


# for x in range(10):
#   x<=100
#   print (x*7)

# for x in range(5):
#     if x < 50:
#         print(x*5)

# recursive function
def factorial(n):
    print(n)
    if n < 2:
        return 1
    result =  n * factorial(n-1)
    return result

factorial(5)

print("BANYAK BELAJAR TENTANG RECURSIVE FUNCTION")