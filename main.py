'''
Lesson goals:
1) Learn variables, loops, functions
2) Learn coming up with an algorithm to solve a problem of determining if a number is prime
3) Introduce a mistake in a program (teacher) and debug the program to fix the mistake (student)
4) Increase difficulty of the program:
   this time find all prime numbers in the range from 1 to 150 and save them in the list
   discuss list data structure with student
5) sum up all numbers containing 9 as a digit
6) This time use list comprehension to sum up all numbers containing 9 as a digit.

'''
primes = []
def is_prime(num):
    for i in range(2, num):
        # if num is divisible by i without remainder, it's not a prime
        if num%i == 0:
            return False
    #says if it's a prime number or not
    return True

# commenting out assignmnet #1
# number = input("Please enter a number to check if it is prime:")
# result = is_prime(int(number))
#says the answer
#print(result)
#if result == True:
#    print("yes, it is a prime number")
#else:
#    print("no, it is not a prime number")

# assignment #2
# find all prime numbers in the range from 1 to 150 and save them in the list

for i in range (1, 100):
    # if i is a prime number, add it to list named primes
    if is_prime(i) == True:
        primes.append(i)

print(primes)

# Lesson 2. Start with no list comprehension
def contains_digit(input_string, digit):
    for ch in input_string:
        if ch == digit:
            return True

# Lesson 2 Use list comprehension
def contains_digit_list_comprehension(input_string, digit):
    return any(ch == digit for ch in input_string)

# not using list comprehension
sum = 0
for p in primes:
    if (contains_digit(str(p), "9")):
        sum = sum + p
print(sum)

# using list comprehension:
# not using list comprehension
sum = 0
for p in primes:
    if (contains_digit_list_comprehension(str(p), "9")):
        sum = sum + p

print(sum)
