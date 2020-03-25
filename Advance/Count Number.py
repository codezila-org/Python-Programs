# * Written By Codezila.org at 20-03-2020 02:25AM (IST)
# Python Program to Count Number of Digits in a Number using While loop

Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)
print("\n\tCode By codezila.org :)\n\tJoin Us On : <github.com/codezila-org>\n\tFor More Mail Us : <contact@codezila.org>")
