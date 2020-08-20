# EX6-1
sample_list = [8, 2, 3, -1, 7]
total = 1

Multiplayer = lambda x,y: x*y

for i in sample_list:
    total = Multiplayer(total,i)

print(total)

#EX6-2
input_Number = int(input('Input a number to compute the factiorial : '))
factorial = lambda x,y: x*y
factorial_resault = 1

for i in range(input_Number):
    factorial_resault = factorial(factorial_resault, i+1)

print(factorial_resault)