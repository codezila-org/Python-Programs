# * Written By Codezila.org at 17-03-2020 10:08AM (IST)
# import complex math module  
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))
print('\n\tCode By codezila.org :)\n\tJoin Us On : <github.com/codezila-org>\n\tFor More Mail Us : <contact@codezila.org>')
