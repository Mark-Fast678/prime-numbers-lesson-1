'''
Lesson goals:
1) Learn variables, loops, functions
2) Learn coming up with an algorithm to solve a problem of determining if a number is prime
3) Introduce a mistake in a program (teacher) and debug the program to fix the mistake (student)
4) Increase difficulty of the program:
   this time find all prime numbers in the range from 1 to 150 and save them in the list
   discuss list data structure with student
5) Bonus points: sum up all numbers containing 9 as a digit. Use list comprehension

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

for i in range (1, 150):
    # if i is a prime number, add it to list named primes
    if is_prime(i) == True:
        primes.append(i)

print(primes)

# Next time continue bonus points challenge to learn about list comprehension
def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

for p in primes:
    if (str(p))