# * Written By Codezila.org at 20-03-2020 1:26AM (IST)
# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
print('\n\tCode By codezila.org :)\n\tJoin Us On : <github.com/codezila-org>\n\tFor More Mail Us : <contact@codezila.org>')
